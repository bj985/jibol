# Nigerian Player Profiling, 2024/25
### Comparing contribution within roles, not just across a goals table

[Back to project hub](../README.md) · [Portfolio](https://ibrahimbolaji.framer.website/)

**Tools:** PostgreSQL · Tableau · Excel  
**Project type:** Independent player-performance analysis

## The question

How can Nigerian players be compared in a way that recognises the different responsibilities of strikers, midfielders and defenders?

This project brings the three positional studies into one series. It examines goal contribution, creativity, progression, defensive actions and aerial performance, supported by written explanations rather than a single universal player score.

## What I built

Player profiles and comparative dashboards, supported by data preparation and SQL analysis. The series separates attacking output from creative contribution, and separates defensive activity from the outcomes of those actions.

| Study | Evaluation focus | Purpose of the comparison |
| --- | --- | --- |
| Strikers | Goal contribution, finishing, chance creation and attacking involvement | Distinguish different ways of contributing to the attack |
| Midfielders | Creativity, passing, ball progression, carrying and defensive contribution | Compare roles without expecting every midfielder to perform the same task |
| Defenders | Defensive actions, aerial-duel activity, duel success and role characteristics | Put defensive output in context instead of equating more actions with better defending |

## Workflow

Source player data → clean and structure tables → calculate and compare metrics in SQL → build positional dashboards → explain the profiles.

FBref and FootyStats feature in the wider player-profiling workflow. The final source inventory should specify the provider, competition, season and extraction date for each released table. Provider data is not redistributed by this case-study page.

## Interpretation guide

Compare rates alongside minutes played. A strong per-90 value over a short sample is not equivalent to sustained output. Keep league, team and positional context visible; do not imply that cross-league numbers are automatically strength-adjusted.

Separate volume from efficiency. A defender's duel volume and success percentage answer different questions. Similarly, goals, expected goals and chance creation should not be treated as interchangeable measures.

Any tiers or role classifications need their thresholds documented alongside the dashboard. They are analytical choices, not official scouting grades.

## Publication status

**Available:** a consolidated case study of the existing striker, midfielder and defender projects.  
**Still to publish here:** original SQL exports, the dataset dictionary, confirmed dashboard links, screenshots and validated result examples.

This page does not claim that the missing working files have been uploaded or that the project uses a predictive recruitment model.
