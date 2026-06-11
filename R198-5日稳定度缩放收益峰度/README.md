# 5日稳定度缩放收益峰度

中文 | [English](#english)

## 中文

`5日稳定度缩放收益峰度` 是一个使用真实行情验证过的 OHLCV 因子 Skill，属于 `分布` 类。

### 因子逻辑

```text
stability(ret_kurt, window=5)
```

该因子将 `收益峰度` 与 `稳定度缩放` 处理结合，观察价格、量能或波动状态在真实市场横截面中的可排序性。

### 真实数据检验

- 样本行数: `196935`
- 可用行数: `195011`
- 覆盖率: `0.9902`
- 5日 Rank IC 均值: `-0.002267`
- 5日 ICIR: `-0.1399`
- 五分组 Q5-Q1 均值: `-0.000435`
- Top 组换手: `0.5436`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`5D Stability Scaled Return Kurtosis` is a real-data-validated framework-neutral OHLCV factor Skill in the `Distribution` family.

### Factor Logic

```text
stability(ret_kurt, window=5)
```

This factor combines `Return Kurtosis` with a `Stability Scaled` transform to test whether the resulting price, volume, or volatility state is cross-sectionally sortable in real market data.

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `195011`
- Coverage: `0.9902`
- 5-day Rank IC mean: `-0.002267`
- 5-day ICIR: `-0.1399`
- Quintile Q5-Q1 mean: `-0.000435`
- Top-quintile turnover: `0.5436`
- No-lookahead check: `True`
- Status: `pass`
