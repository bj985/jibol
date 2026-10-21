"""Home teams leading at half-time and winning at full-time.

Uses football-data.org v4. Live access requires FOOTBALL_DATA_API_KEY.
Only finished, regular-time matches with complete integer scores are eligible.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def summarize_matches(matches: list) -> tuple[list[dict], int]:
    """Return team counts/rates and number of excluded input rows.

    Rate denominator: eligible home matches for that team, not all fixtures.
    Duplicate match IDs, unfinished matches and missing scores are excluded.
    """
    if not isinstance(matches, list):
        raise ValueError("Expected a list of matches.")
    played, wins, names, seen = Counter(), Counter(), {}, set()
    excluded = 0
    for match in matches:
        if not isinstance(match, dict):
            excluded += 1
            continue
        match_id = match.get("id")
        team, score = match.get("homeTeam"), match.get("score")
        if not isinstance(team, dict) or not isinstance(score, dict):
            excluded += 1
            continue
        ht, ft = score.get("halfTime"), score.get("fullTime")
        if not isinstance(ht, dict) or not isinstance(ft, dict):
            excluded += 1
            continue
        values = [ht.get("home"), ht.get("away"), ft.get("home"), ft.get("away")]
        team_id, name = team.get("id"), team.get("name")
        valid = (match.get("status") == "FINISHED"
                 and score.get("duration") == "REGULAR"
                 and type(match_id) is int and match_id > 0
                 and type(team_id) is int and team_id > 0
                 and isinstance(name, str) and bool(name.strip())
                 and all(type(v) is int and v >= 0 for v in values))
        if not valid or match_id in seen:
            excluded += 1
            continue
        seen.add(match_id)
        names[team_id] = name.strip()
        played[team_id] += 1
        if values[0] > values[1] and values[2] > values[3]:
            wins[team_id] += 1
    rows = [{"team_id": tid, "team": names[tid], "eligible_home_matches": n,
             "ht_ft_home_wins": wins[tid],
             "ht_ft_home_win_pct": round(100 * wins[tid] / n, 2)}
            for tid, n in played.items()]
    rows.sort(key=lambda r: (-r["ht_ft_home_win_pct"], -r["eligible_home_matches"], r["team"]))
    return rows, excluded


def fetch_matches(competition: str, season: int | None = None) -> list:
    """Fetch matches using HTTPS and an environment-based credential."""
    token = os.environ.get("FOOTBALL_DATA_API_KEY", "").strip()
    if not token:
        raise ValueError("Set FOOTBALL_DATA_API_KEY before requesting live data.")
    if not re.fullmatch(r"[A-Z0-9]+", competition):
        raise ValueError("Competition must be an uppercase API code or numeric ID.")
    if season is not None and season < 1870:
        raise ValueError("Season must be a valid starting year.")
    params = {"status": "FINISHED"}
    if season is not None:
        params["season"] = str(season)
    url = f"https://api.football-data.org/v4/competitions/{competition}/matches?{urlencode(params)}"
    request = Request(url, headers={"X-Auth-Token": token})
    try:
        with urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except HTTPError as exc:
        raise ValueError(f"API request failed (HTTP {exc.code}); check access and rate limits.") from None
    except (URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise ValueError("API request failed or returned invalid JSON.") from None
    if not isinstance(payload, dict) or not isinstance(payload.get("matches"), list):
        raise ValueError("API response does not contain a matches list.")
    return payload["matches"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--competition", default="PL", help="API code, default PL")
    parser.add_argument("--season", type=int, help="Season starting year; otherwise the API default")
    parser.add_argument("--input", type=Path, help="Local JSON response; bypasses the API")
    args = parser.parse_args(argv)
    try:
        if args.input:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
            if not isinstance(payload, dict) or "matches" not in payload:
                raise ValueError("Local JSON must contain a matches list.")
            matches = payload["matches"]
        else:
            matches = fetch_matches(args.competition, args.season)
        rows, excluded = summarize_matches(matches)
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    fields = ["team_id", "team", "eligible_home_matches", "ht_ft_home_wins", "ht_ft_home_win_pct"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    print(f"Input rows: {len(matches)}; eligible: {sum(r['eligible_home_matches'] for r in rows)}; excluded: {excluded}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
