# India OpenRisk

India OpenRisk is a pre-market risk-intelligence platform for Indian equity investors. Before the Indian market opens, it converts verified U.S. market movements and selected U.S. news into an explainable assessment of next-session Nifty 50 opening risk.

> This is a risk-preparation tool, not a price-prediction or trading-recommendation system.

## Version 1

- **Inputs:** S&P 500, Nasdaq-100, VIX, U.S. 10-year Treasury yield, selected U.S. news, and historical Nifty 50 data.
- **Output:** probability of normal, elevated, or high Nifty opening risk; evidence, confidence, and limitations.
- **Out of scope:** exact price predictions, automated trades, and individual-stock recommendations.

## What is in this folder?

- [`PROJECT.md`](PROJECT.md) — the project plan, scope, decisions, and phase checklist.
- [`src/openrisk/`](src/openrisk/) — application code as we build it.
- [`tests/`](tests/) — automated checks.

Data, reports, and exploratory notebooks will be added only when we actually start using them.

## Local setup

```bash
uv sync --all-groups
cp .env.example .env
```

Add API credentials to `.env` only when a phase requires them.

## Project plan

See [PROJECT.md](PROJECT.md).
   - [`docs/risk-disclaimer.md`](docs/risk-disclaimer.md) — what this tool does and does not promise.