# Nigeria Super Eagles Performance Analysis
### 1994–2026 | Results, rankings and national-team context

[Back to project hub](../README.md) · [Portfolio](https://ibrahimbolaji.framer.website/)

**Tools:** Power BI · DAX · Excel · Power Query  
**Project type:** Historical national-team performance dashboard

## The question

How has Nigeria's national-team performance changed across competitions, opponents, coaching periods and eras?

The project connects tournament history with match results, goals, opponents, rankings and coaching timelines. Its purpose is to make long-term comparisons accessible without reducing the team's history to trophies alone.

## What I built

A Power BI dashboard and performance report using prepared historical datasets, measures, filters and comparative visuals.

| Analysis area | What it helps a reader investigate |
| --- | --- |
| Results and scoring | Wins, draws, losses, goals scored and conceded, and changes over time |
| Tournament performance | AFCON, World Cup and other competition context |
| Opponents and head-to-head records | How results vary across opponents and regions |
| Coaching periods | Results in their correct managerial and competition context |
| Rankings | Changes in recorded ranking positions alongside performance history |

## Data decisions that matter

Manager assignments must follow the relevant match dates and competitions. A year containing more than one coach cannot be represented reliably by assigning one manager to every match.

Different date windows and competition filters change the denominator of a win percentage. Rankings should be treated as historical snapshots, not averaged or summed without an explicit purpose. A penalty-shootout outcome must not silently change the chosen statistical definition of a draw.

The project range is 1994–2026. Each published table should state its actual coverage; the project title does not mean every indicator has observations on every date.

## Why this project matters

It demonstrates the reporting workflow from data preparation and model organisation to measure design and visual communication. The football interpretation is grounded in the selected competition and time period rather than comparisons stripped of context.

## Publication status

**Available:** project overview and interpretation notes.  
**Still to publish here:** the original Power BI model or public dashboard link, selected DAX measures, source inventory, dashboard screenshots and checked result examples.

The formulas and working datasets have not been reconstructed from memory for this page.
