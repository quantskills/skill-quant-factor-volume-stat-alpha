---
name: quant-real-factor-5d-volume-confirmed-volume-ts-rank
description: Use when computing the 5D Volume Confirmed Volume TS Rank factor from user-supplied real OHLCV data or reviewing its bundled real-data validation metrics.
metadata:
  organization: QuantSkills
  organization_url: https://github.com/quantskills
  repository: skill-quant-factor-volume-stat-alpha
  repository_url: https://github.com/quantskills/skill-quant-factor-volume-stat-alpha
  collection: volume-stat-alpha
  factor_id: R229
  category: Time Series Rank
  license: GPL-3.0-only
  copyright: Copyright (C) 2026 QuantSkills
---

# 5D Volume Confirmed Volume TS Rank

Use this Skill to compute `5日量能确认成交量时序排名` / `5D Volume Confirmed Volume TS Rank` from caller-provided OHLCV data.

## Workflow

1. Load a `pandas.DataFrame` with `open`, `high`, `low`, `close`, `volume`; include `date` and `symbol` for cross-sectional research.
2. Call `scripts/factor.py::compute_factor(df)` to compute the factor column.
3. Call `generate_signals(df)` for a simple rank-based long/short signal.
4. Review `validation_real/report.md` before using the factor in a model.

## Runtime Contract

- Framework-neutral Python: `pandas` and `numpy`.
- The caller owns data vendor, universe, calendar, costs, slippage, and execution modeling.
