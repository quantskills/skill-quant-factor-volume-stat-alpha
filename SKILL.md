---
name: quant-factor-volume-stat-alpha
description: Use when an agent needs a verified library of OHLCV volume, volume-price,
  ranking, and statistical alpha factor Skills for liquidity and distribution research.
quantSkills:
  project_type: skill
  category: factor
  tags:
  - alpha-factor
  - volume
  - volume-price
  - ranking
  - statistics
  platforms:
  - claude-code
  - codex
  - openclaw
  - cursor
  status: stable
  validation_level: verified
  maintainer_type: official
  summary_zh: 量能、量价和统计排序类因子库：216 个独立 OHLCV 因子 Skill，真实行情验证 216/216 全部通过。
  summary_en: Volume, volume-price, ranking, and statistical OHLCV alpha factor library
    with 216 factor Skills validated on real market data.
  license: GPL-3.0
---

# Quant Factor Volume Stat Alpha

Use this skill when an agent needs to select, inspect, or apply OHLCV volume, volume-price, ranking, and statistical alpha factor Skills from this repository.

## Workflow

1. Read [README.md](README.md) for the repository-level inventory, validation scope, and market sample.
2. Use `factor_index.json` to locate the relevant factor family or individual factor directory.
3. Open the selected factor folder under the factors directory and follow its local instructions before writing or running code.
4. Treat validation metrics as historical research evidence, not investment advice. Re-run validation when the universe, time range, data vendor, or execution assumptions change.

## Scope

This repository focuses on liquidity, volume expansion or contraction, volume-price interaction, time-series ranking, and return-distribution signals built from OHLCV data.
