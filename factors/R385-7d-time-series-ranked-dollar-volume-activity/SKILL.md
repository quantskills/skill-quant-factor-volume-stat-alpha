---
name: quant-real-factor-7d-time-series-ranked-dollar-volume-activity
description: Use when computing the 7D Time-Series Ranked Dollar Volume Activity factor from user-supplied real OHLCV data or reviewing its bundled real-data validation metrics.
metadata:
  organization: QuantSkills
  organization_url: https://github.com/quantskills
  repository: skill-quant-factor-volume-stat-alpha
  repository_url: https://github.com/quantskills/skill-quant-factor-volume-stat-alpha
  collection: volume-stat-alpha
  factor_id: R385
  category: Liquidity
  license: GPL-3.0-only
  copyright: Copyright (C) 2026 QuantSkills
---

# 7D Time-Series Ranked Dollar Volume Activity

Use this Skill to compute `7日时序排名成交额活跃度` / `7D Time-Series Ranked Dollar Volume Activity` from caller-provided OHLCV data.

## Workflow

1. Load a `pandas.DataFrame` with `open`, `high`, `low`, `close`, `volume`; include `date` and `symbol` for cross-sectional research.
2. Call `scripts/factor.py::compute_factor(df)` to compute the factor column.
3. Call `generate_signals(df)` for a simple rank-based long/short signal.
4. Review `validation_real/report.md` before using the factor in a model.

## Runtime Contract

- Framework-neutral Python: `pandas` and `numpy`.
- The caller owns data vendor, universe, calendar, costs, slippage, and execution modeling.
