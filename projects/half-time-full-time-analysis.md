# Half-Time / Full-Time Home Results
### A small Python analysis with a clearly defined denominator

[Back to project hub](../README.md) · [Source code](../Task%201.py) · [Tests](../tests/test_home_results.py)

## Question and calculation

For each team, what percentage of its eligible home matches did it lead at half-time and win at full-time?

`HT/FT home-win percentage = qualifying home matches / eligible home matches × 100`

This is a joint outcome rate. It is **not** the percentage of half-time leads that were converted into wins. That conditional metric would require a different denominator.

An eligible row has status `FINISHED`, duration `REGULAR`, valid match/team IDs and complete non-negative integer half-time and full-time scores. Repeated match IDs are counted once. Teams with no qualifying wins remain in the output with a zero rate. The excluded-row count is printed to standard error.

## Run locally

Python 3.10 or newer is required. The code uses the standard library only.

```bash
python -m unittest discover -s tests -v
python "Task 1.py" --input path/to/matches.json > results.csv
```

The local JSON input must have the same top-level structure as an API response: an object containing a `matches` list.

For live access, set `FOOTBALL_DATA_API_KEY` locally to your own current football-data.org credential. Never paste a real key into the script or commit it. Then run:

```bash
python "Task 1.py" --competition PL --season 2024 > results.csv
```

The year is the season's starting year; omit it to use the API's default season. Historical access depends on the provider's account permissions. Requests use HTTPS and a timeout.

## Output

CSV columns: `team_id`, `team`, `eligible_home_matches`, `ht_ft_home_wins`, `ht_ft_home_win_pct`.

## Testing and limitations

The 13 automated tests use synthetic fixtures and a mocked network call. They test denominators, zero-win teams, missing scores, non-finished matches, duplicate IDs, extra time, malformed records, input immutability, missing credentials, request configuration and CLI error handling.

The tests passed locally during this repository update. A live API call was not performed and no historical results are claimed. Missing score coverage can bias comparisons; inspect the exclusion count before using the output. Extra-time and shootout matches are deliberately excluded.

The existing exercise was refactored during the portfolio update to remove embedded credentials, correct the denominator and add tests. This maintenance work is distinct from the original project version.

## Provider documentation

[football-data.org competition resource](https://docs.football-data.org/general/v4/competition.html)
