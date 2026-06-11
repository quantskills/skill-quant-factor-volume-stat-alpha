# 5日压缩成交额活跃度

中文 | [English](#english)

## 中文

`5日压缩成交额活跃度` 是一个使用真实行情验证过的 OHLCV 因子 Skill，属于 `流动性` 类。

### 因子逻辑

```text
compress(dollar_volume, window=5)
```

该因子将 `成交额活跃度` 与 `压缩` 处理结合，观察价格、量能或波动状态在真实市场横截面中的可排序性。

### 真实数据检验

- 样本行数: `196935`
- 可用行数: `196047`
- 覆盖率: `0.9955`
- 5日 Rank IC 均值: `0.005804`
- 5日 ICIR: `0.2454`
- 五分组 Q5-Q1 均值: `0.000761`
- Top 组换手: `0.7045`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`5D Compressed Dollar Volume Activity` is a real-data-validated framework-neutral OHLCV factor Skill in the `Liquidity` family.

### Factor Logic

```text
compress(dollar_volume, window=5)
```

This factor combines `Dollar Volume Activity` with a `Compressed` transform to test whether the resulting price, volume, or volatility state is cross-sectionally sortable in real market data.

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `196047`
- Coverage: `0.9955`
- 5-day Rank IC mean: `0.005804`
- 5-day ICIR: `0.2454`
- Quintile Q5-Q1 mean: `0.000761`
- Top-quintile turnover: `0.7045`
- No-lookahead check: `True`
- Status: `pass`
