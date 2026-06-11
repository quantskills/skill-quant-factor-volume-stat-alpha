# 5日时序排名收益偏度

中文 | [English](#english)

## 中文

`5日时序排名收益偏度` 是一个使用真实行情验证过的 OHLCV 因子 Skill，属于 `分布` 类。

### 因子逻辑

```text
rank(ret_skew, window=5)
```

该因子将 `收益偏度` 与 `时序排名` 处理结合，观察价格、量能或波动状态在真实市场横截面中的可排序性。

### 真实数据检验

- 样本行数: `196935`
- 可用行数: `195159`
- 覆盖率: `0.9910`
- 5日 Rank IC 均值: `0.001099`
- 5日 ICIR: `0.0626`
- 五分组 Q5-Q1 均值: `0.000018`
- Top 组换手: `0.5107`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`5D Time-Series Ranked Return Skewness` is a real-data-validated framework-neutral OHLCV factor Skill in the `Distribution` family.

### Factor Logic

```text
rank(ret_skew, window=5)
```

This factor combines `Return Skewness` with a `Time-Series Ranked` transform to test whether the resulting price, volume, or volatility state is cross-sectionally sortable in real market data.

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `195159`
- Coverage: `0.9910`
- 5-day Rank IC mean: `0.001099`
- 5-day ICIR: `0.0626`
- Quintile Q5-Q1 mean: `0.000018`
- Top-quintile turnover: `0.5107`
- No-lookahead check: `True`
- Status: `pass`

## License

This factor Skill is licensed under the GNU General Public License v3.0.

Copyright (C) 2026 QuantSkills.
