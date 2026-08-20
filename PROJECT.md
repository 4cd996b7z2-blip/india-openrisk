# India OpenRisk — Project Plan

## What we are building

Before Indian markets open, India OpenRisk reads verified U.S. market movements and selected U.S. news, estimates the next Nifty 50 session's opening-risk level, and explains the evidence behind that assessment.

It is a risk-preparation tool, not a price-prediction or trading-recommendation system.

## Version 1

- **U.S. inputs:** S&P 500, Nasdaq-100, VIX, U.S. 10-year Treasury yield, and selected U.S. news.
- **Indian target:** Nifty 50 opening risk.
- **Risk levels:** normal, elevated, and high.
- **Output:** risk probability, confidence, evidence, and limitations.

## Rules

- The numerical risk forecast comes from a tested statistical model.
- AI1 selects and classifies cited overnight evidence; it can say there is no material news.
- AI2 writes the final report using only verified data and model output.
- We use time-based backtests and report failures honestly.
- We do not predict exact prices or issue buy/sell calls.

## Phases

1. **Foundation** — environment, repository, project definition. ✅
2. **Data** — choose sources; collect and validate U.S. and Nifty history.
3. **Research** — define high-risk days and analyse historical relationships.
4. **Baselines** — build simple risk rules and benchmarks.
5. **Risk model** — train, test, calibrate, and document the model.
6. **AI evidence** — add cited U.S. news selection.
7. **Morning brief** — produce the final plain-English report and charts.
8. **Dashboard** — automate daily runs and present results.
9. **Portfolio impact** — optional later release.

## Before each phase is pushed to GitHub

1. Finish the phase deliverables.
2. Update this file with material decisions and limitations.
3. Run relevant tests and code-quality checks.
4. Check that no API keys, downloaded data, or generated reports are included.
5. Commit using `phase-N: <outcome>` and push to GitHub.

## Decisions so far

| Date | Decision | Why |
| --- | --- | --- |
| 2026-08-20 | Version 1 uses U.S. inputs only. | Keep the first release focused and finishable. |
| 2026-08-20 | Predict risk levels, not prices. | More useful and more defensible. |
| 2026-08-20 | Separate AI from the risk score. | Keep the forecast measurable and testable. |
| 2026-08-20 | Push a reviewed release after every completed phase. | Maintain a clean, auditable project history. |
