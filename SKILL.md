---
name: quant-factor-volume-stat-alpha
description: Use when an agent needs a verified library of OHLCV volume, volume-price,
  ranking, and statistical alpha factor Skills for liquidity and distribution research.
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
  - hermes
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

```json qsh-form
{
  "version": 1,
  "task": {
    "placeholder": "补充 OHLCV 数据位置、研究区间或希望筛选的量价/统计因子特征（可选）"
  },
  "fields": [
    {
      "key": "factor",
      "label": "因子名/主题线索 (可选)",
      "type": "text",
      "placeholder": "例如：量能扩缩类、量价互动类、时序排名类、收益分布类",
      "help": "运行时经本库 factor_index.json 定位具体因子"
    },
    {
      "key": "expr",
      "label": "自定义因子表达式",
      "type": "textarea",
      "placeholder": "例如：-1 * correlation(rank(open), rank(volume), 10)"
    },
    {
      "key": "universe",
      "label": "股票池",
      "type": "select",
      "default": "000300.SH",
      "options": [
        { "value": "000300.SH", "label": "沪深300" },
        { "value": "000905.SH", "label": "中证500" },
        { "value": "399006.SZ", "label": "创业板指" },
        { "value": "000852.SH", "label": "中证1000" }
      ]
    },
    {
      "key": "horizon",
      "label": "预测周期",
      "type": "select",
      "default": "5",
      "options": [
        { "value": "1", "label": "未来1日" },
        { "value": "5", "label": "未来5日" },
        { "value": "10", "label": "未来10日" }
      ]
    }
  ],
  "prompt_template": "{{#task}}任务与材料：\n{{task}}\n\n{{/task}}{{#attachments}}用户上传的材料（已放入工作区）：\n{{attachments}}\n\n{{/attachments}}从已验证的 OHLCV 成交量、量价、排名和统计因子库中选择并应用因子。{{#factor}}因子名/主题线索：{{factor}}。{{/factor}}{{#expr}}自定义表达式优先：{{expr}}。{{/expr}}在 {{universe}} 上按 {{horizon}} 日预测周期复核数据字段、因子定义和历史验证适用性；若股票池、区间、数据源或执行假设变化则重新验证，输出中文报告。"
}
```

# Quant Factor Volume Stat Alpha

Use this skill when an agent needs to select, inspect, or apply OHLCV volume, volume-price, ranking, and statistical alpha factor Skills from this repository.

## Workflow

1. Read [README.md](README.md) for the repository-level inventory, validation scope, and market sample.
2. Use `factor_index.json` to locate the relevant factor family or individual factor directory.
3. Open the selected factor folder under the factors directory and follow its local instructions before writing or running code.
4. Treat validation metrics as historical research evidence, not investment advice. Re-run validation when the universe, time range, data vendor, or execution assumptions change.

## Scope

This repository focuses on liquidity, volume expansion or contraction, volume-price interaction, time-series ranking, and return-distribution signals built from OHLCV data.
## Agent Compatibility

- Claude Code, Codex, Hermes, and OpenClaw can load this root folder as a collection skill, then drill into actors/*/SKILL.md.
- Cursor should use gents/cursor-rule.mdc and keep the full repository under .cursor/skills/quant-factor-volume-stat-alpha.
- Agents without native skill discovery can paste gents/portable-loader.md.
