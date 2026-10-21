"""Synthetic fixtures test the calculation; they are not real match results."""
import copy
import io
import os
import runpy
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from unittest.mock import patch

MODULE = runpy.run_path(str(Path(__file__).resolve().parents[1] / "Task 1.py"))
summarize = MODULE["summarize_matches"]
fetch = MODULE["fetch_matches"]
main = MODULE["main"]


def fixture(mid=1, team_id=10, ht=(1, 0), ft=(2, 0), status="FINISHED"):
    return {"id": mid, "status": status,
            "homeTeam": {"id": team_id, "name": f"Synthetic Team {team_id}"},
            "score": {"duration": "REGULAR", "halfTime": dict(zip(("home", "away"), ht)),
                      "fullTime": dict(zip(("home", "away"), ft))}}


class HomeResultsTests(unittest.TestCase):
    def test_rate_uses_team_home_denominator(self):
        rows, excluded = summarize([fixture(), fixture(2, ht=(0, 0)), fixture(3, team_id=20)])
        by_id = {r["team_id"]: r for r in rows}
        self.assertEqual(by_id[10]["ht_ft_home_win_pct"], 50)
        self.assertEqual(by_id[20]["ht_ft_home_win_pct"], 100)
        self.assertEqual(excluded, 0)

    def test_zero_success_team_is_retained(self):
        rows, _ = summarize([fixture(ht=(0, 1), ft=(1, 1))])
        self.assertEqual(rows[0]["ht_ft_home_wins"], 0)
        self.assertEqual(rows[0]["ht_ft_home_win_pct"], 0)

    def test_incomplete_scores_are_excluded(self):
        rows, excluded = summarize([fixture(ht=(None, None))])
        self.assertEqual((rows, excluded), ([], 1))

    def test_scheduled_match_is_excluded(self):
        self.assertEqual(summarize([fixture(status="SCHEDULED")]), ([], 1))

    def test_duplicate_ids_count_once(self):
        rows, excluded = summarize([fixture(), fixture()])
        self.assertEqual(rows[0]["eligible_home_matches"], 1)
        self.assertEqual(excluded, 1)

    def test_extra_time_is_excluded(self):
        m = fixture()
        m["score"]["duration"] = "EXTRA_TIME"
        self.assertEqual(summarize([m]), ([], 1))

    def test_boolean_and_negative_scores_are_rejected(self):
        self.assertEqual(summarize([fixture(ht=(True, 0)), fixture(2, ft=(-1, 0))]), ([], 2))

    def test_malformed_rows_are_excluded(self):
        self.assertEqual(summarize([None, {}, {"score": None}]), ([], 3))

    def test_empty_input_is_safe(self):
        self.assertEqual(summarize([]), ([], 0))
        with self.assertRaises(ValueError):
            summarize({})

    def test_inputs_are_not_modified(self):
        matches = [fixture()]
        snapshot = copy.deepcopy(matches)
        summarize(matches)
        self.assertEqual(matches, snapshot)

    def test_missing_key_fails_without_network(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "FOOTBALL_DATA_API_KEY"):
                fetch("PL")

    def test_network_request_uses_https_timeout_and_header(self):
        class Response(io.StringIO):
            pass
        with patch.dict(os.environ, {"FOOTBALL_DATA_API_KEY": "synthetic-test-token"}):
            with patch.dict(fetch.__globals__, {"urlopen": lambda req, timeout: self._check_request(req, timeout, Response)}):
                self.assertEqual(fetch("PL", 2024), [])

    def _check_request(self, req, timeout, response_type):
        self.assertTrue(req.full_url.startswith("https://api.football-data.org/"))
        self.assertIn("season=2024", req.full_url)
        self.assertEqual(timeout, 30)
        self.assertEqual(req.get_header("X-auth-token"), "synthetic-test-token")
        return response_type('{"matches": []}')

    def test_cli_reports_missing_key(self):
        with patch.dict(os.environ, {}, clear=True), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(main([]), 1)


if __name__ == "__main__":
    unittest.main()
