# Bolaji Ibrahim Ajibola
### Football Data Analysis | Player Profiling | Business Intelligence

I turn football data into structured analysis, interactive dashboards and written reports, with a particular interest in Nigerian players and African football.

My projects connect data preparation, SQL analysis and visual reporting with questions about player roles, national-team performance and tournament development.

[Portfolio](https://ibrahimbolaji.framer.website/) · [LinkedIn](https://www.linkedin.com/in/ajibola-bolaji/) · [GitHub](https://github.com/bj985)

## Explore my work

| Project | Analytical focus | Available here |
| --- | --- | --- |
| [FIFA World Cup Historical Analysis](https://github.com/bj985/fifa-world-cup-historical-analysis) | Tournament development, attendance, scoring and national-team performance; project coverage 1930–2026 | Dedicated repository |
| [AFCON Historical Performance Analysis](https://github.com/bj985/afcon-historical-performance-analysis) | Regional dominance, hosting, consistency and stadium attendance | Dedicated repository |
| [Nigerian Player Profiling, 2024/25](projects/nigerian-player-performance-analysis.md) | Strikers, midfielders and defenders evaluated through position-specific metrics | Project case study |
| [Super Eagles Performance, 1994–2026](projects/super-eagles-performance-analysis.md) | Results, competition history, coaching periods and ranking trends | Project case study |
| [Benjamin Fredrick Player Analysis](projects/benjamin-fredrick-player-analysis.md) | Belgian Pro League profiling alongside separate Nigeria video observations | Project case study |
| [Ademola Lookman Performance Analysis](projects/ademola-lookman-performance-analysis.md) | Finishing, creativity, dribbling and attacking contribution | Project case study |
| [Half-Time / Full-Time Home Results](projects/half-time-full-time-analysis.md) | A Python API exercise with explicit denominators and data-quality checks | Runnable code and automated tests |

The four player and national-team case studies document existing portfolio work. Their original SQL exports, dashboard files and verified numerical outputs are not bundled here yet. The Python exercise is runnable; live API access requires the user's own credential. Each project page states its publication status.

## How I work

**Collect and prepare data → investigate with SQL → build dashboards → explain the football implications.**

| Area | Tools and focus |
| --- | --- |
| Data preparation | Excel, Power Query, source reconciliation and structured datasets |
| Analysis | PostgreSQL, joins, aggregations, window functions and reporting views |
| Visual reporting | Power BI, DAX, Tableau and readable dashboard narratives |
| Football interpretation | Player profiling, role comparisons, national-team trends and tactical observation |
| Video analysis | Once Sport for independent projects; club data and national-team footage remain separate evidence sources |

My background in economics, finance and operations informs the way I frame questions, check calculations and communicate findings. I hold an MSc in Football Data Analytics and a BSc in Economics.

## Run the Python exercise

Requires Python 3.10 or newer. No third-party packages are required.

```bash
python -m unittest discover -s tests -v
python "Task 1.py" --input path/to/matches.json > results.csv
```

For live API usage and metric definitions, see the [exercise guide](projects/half-time-full-time-analysis.md).

## Repository guide

`projects/` contains the case studies. `Task 1.py` contains the API exercise. `tests/` contains synthetic test cases, not historical match results. `PROFILE.md` is prepared profile-page copy; it is not the active GitHub profile README.

Read the [publication status](docs/publication-status.md) for the distinction between available documentation, tested code and supporting assets still to be published.
