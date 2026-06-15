---
name: quant-factor-volume-stat-alpha
description: Use when selecting, inspecting, validating, or applying the QuantSkills volume-stat OHLCV alpha factor collection, including volume, price-volume, liquidity, time-series-rank, and return-distribution factors; use for factor discovery, factor_index navigation, compute_factor usage, validation review, or mapping a volume/statistical alpha idea to a packaged factor Skill.
license: GPL-3.0-only
metadata:
  organization: QuantSkills
  organization_url: https://github.com/quantskills
  repository: skill-quant-factor-volume-stat-alpha
  repository_url: https://github.com/quantskills/skill-quant-factor-volume-stat-alpha
  project_type: skill
  collection: quant-factor-volume-stat-alpha
  creator: abgyjaguo
  maintainer: abgyjaguo
---

# Quant Factor Volume Stat Alpha

Use this collection-level skill to navigate the packaged factor library before loading an individual factor skill.

## Workflow

1. Read `factor_index.json` first to search by factor id, English slug, category, base signal, transform, formula, or path.
2. Use `repo_summary.json` and `validation_summary_real.json` to understand collection-level coverage and real-market validation status.
3. Pick a concrete factor folder under `factors/`, then read that factor's `SKILL.md` and `references/formula.md`.
4. To apply a factor, import `compute_factor(df)` from the selected factor's `scripts/factor.py`; the input data must include `date`, `symbol`, `open`, `high`, `low`, `close`, and `volume`.
5. To verify a selected factor, run `python scripts/validate.py` from inside the factor folder and compare the output with `validation_real/result.json` and `validation_real/report.md`.
6. Preserve the original factor id and folder name in reports so users can trace results back to the packaged skill.

## Scope

This repository contains 216 standalone factor skills focused on volume, price-volume, liquidity, time-series-rank, and return-distribution OHLCV alpha factors. Each factor is framework-neutral and works on standard OHLCV data.

## Agent Compatibility

- Claude Code, Codex, Hermes, and OpenClaw can load this root folder as a collection skill, then drill into `factors/*/SKILL.md`.
- Cursor should use `agents/cursor-rule.mdc` and keep the full repository under `.cursor/skills/quant-factor-volume-stat-alpha`.
- Agents without native skill discovery can paste `agents/portable-loader.md`.
