# India OpenRisk — Project Plan

## What we are building

Before Indian markets open, India OpenRisk builds a scalable data pipeline over U.S. market data, broad equity-universe pricing, and Nifty history, then uses statistical analysis and modeling to estimate the next Nifty 50 session's opening-risk level — with the evidence and methodology behind that assessment fully documented and reproducible.

It is a data-analysis and risk-modeling project first, not an AI-agent system. Any AI-generated narrative is an optional finishing layer on top of a rigorous data pipeline, not the core of the project.

## Version 1

- **U.S. inputs:** S&P 500, Nasdaq-100, VIX, U.S. 10-year Treasury yield, and (later) constituent-level pricing across the S&P 500.
- **Indian inputs:** Nifty 50 history, and (later) Nifty 500 constituents for sector-level analysis.
- **Risk levels:** normal, elevated, and high.
- **Output:** risk probability, confidence, key statistical drivers, and limitations.

## Rules

- The numerical risk forecast comes from a tested statistical/ML model, backed by a documented, versioned data pipeline.
- Data is stored in partitioned, queryable form (not ad-hoc CSVs) so the pipeline scales to a wide ticker universe.
- Every model is benchmarked against simple baselines and time-based backtests; failures are reported honestly.
- An optional AI narrative layer (Phase 10) may summarize model output and cited news, but never replaces or obscures the underlying data/model evidence.
- We do not predict exact prices or issue buy/sell calls.

## Phases

0. **Foundation** — environment, repository, project definition. ✅
1. **Data architecture & sourcing** — choose sources; define schema across a wide ticker universe, not just index level.
2. **Ingestion pipeline at scale** — partitioned Parquet storage, Polars/DuckDB-based pipeline, fact/dimension structure.
3. **Exploratory data analysis at scale** — distribution, correlation, and sector-level analysis across the full dataset.
4. **Feature engineering pipeline** — reusable, versioned features (volatility, momentum, lagged returns, cross-asset correlation).
5. **Baseline models** — simple rules any real model must beat.
6. **Risk model** — train, calibrate, and validate across the full dataset.
7. **Rigorous backtesting & evaluation** — time-based validation, performance by sector/regime.
8. **Analytics dashboard** — interactive, drill-down from index to sector to ticker level.
9. **Automation & orchestration** — scheduled runs, data-quality monitoring, tests.
10. **Optional AI narrative layer** — cited evidence + plain-English brief, as a finishing touch, not the core.

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
| 2026-09-11 | Pivoted scope from AI-agent-led risk brief to data-analysis/big-data-led pipeline; AI narrative moved to optional final phase. | Better demonstrates data engineering and statistical rigor over LLM orchestration. |