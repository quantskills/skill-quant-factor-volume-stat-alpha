# 7日时序排名OBV斜率

中文 | [English](#english)

## 中文

`7日时序排名OBV斜率` 是一个使用真实行情验证过的 OHLCV 因子 Skill，属于 `量价` 类。

### 因子逻辑

```text
rank(obv_slope, window=7)
```

该因子将 `OBV斜率` 与 `时序排名` 处理结合，观察价格、量能或波动状态在真实市场横截面中的可排序性。

### 真实数据检验

- 样本行数: `196935`
- 可用行数: `194715`
- 覆盖率: `0.9887`
- 5日 Rank IC 均值: `0.002172`
- 5日 ICIR: `0.0875`
- 五分组 Q5-Q1 均值: `0.000767`
- Top 组换手: `0.3270`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`7D Time-Series Ranked OBV Slope` is a real-data-validated framework-neutral OHLCV factor Skill in the `Price Volume` family.

### Factor Logic

```text
rank(obv_slope, window=7)
```

This factor combines `OBV Slope` with a `Time-Series Ranked` transform to test whether the resulting price, volume, or volatility state is cross-sectionally sortable in real market data.

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `194715`
- Coverage: `0.9887`
- 5-day Rank IC mean: `0.002172`
- 5-day ICIR: `0.0875`
- Quintile Q5-Q1 mean: `0.000767`
- Top-quintile turnover: `0.3270`
- No-lookahead check: `True`
- Status: `pass`
