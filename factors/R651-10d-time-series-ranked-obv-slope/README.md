# 10日时序排名OBV斜率

中文 | [English](#english)

## 中文

`10日时序排名OBV斜率` 是一个框架中立的 OHLCV 因子 Skill，属于 `量价` 类。它只依赖用户传入的行情字段，不绑定任何交易框架或数据供应商。

### 因子逻辑

```text
rank(obv_slope, window=10)
```

该因子把“OBV斜率”与“时序排名”处理结合，用来刻画价格、量能或波动状态在横截面上的可排序性。

### 能做什么

- 从 `open/high/low/close/volume` 计算一个可排序的横截面因子值
- 输出简单的分位数多空信号，方便 agent 做研究原型
- 可嵌入用户自己的数据源、股票池、调仓频率和交易成本模型

### 真实数据验证

- 样本行数: `196935`
- 可用行数: `194271`
- 市场覆盖: `{"cn": 98, "us": 50}`
- 覆盖率: `0.9865`
- 5日 Rank IC 均值: `0.011911`
- 5日 ICIR: `0.4983`
- 五分组 Q5-Q1 均值: `0.002019`
- Top 组换手: `0.2583`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`10D Time-Series Ranked OBV Slope` is a framework-neutral OHLCV factor Skill in the `Price Volume` family. It depends only on caller-supplied market fields and is not tied to any trading framework or data vendor.

### Factor Logic

```text
rank(obv_slope, window=10)
```

This factor combines OBV Slope with a Time-Series Ranked transform to test cross-sectional sortability in price, volume, or volatility states.

### What It Does

- Computes a cross-sectionally sortable factor from `open/high/low/close/volume`
- Emits simple quantile long/short prototype signals for agent research workflows
- Lets the caller plug in their own data source, universe, rebalance calendar, and cost model

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `194271`
- Markets: `{"cn": 98, "us": 50}`
- Coverage: `0.9865`
- 5-day Rank IC mean: `0.011911`
- 5-day ICIR: `0.4983`
- Quintile Q5-Q1 mean: `0.002019`
- Top-quintile turnover: `0.2583`
- No-lookahead check: `True`
- Status: `pass`

## License

This factor Skill is licensed under the GNU General Public License v3.0.

Copyright (C) 2026 QuantSkills.
