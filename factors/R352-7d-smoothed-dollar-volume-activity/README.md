# 7日平滑成交额活跃度

中文 | [English](#english)

## 中文

`7日平滑成交额活跃度` 是一个使用真实行情验证过的 OHLCV 因子 Skill，属于 `流动性` 类。

### 因子逻辑

```text
smooth(dollar_volume, window=7)
```

该因子将 `成交额活跃度` 与 `平滑` 处理结合，观察价格、量能或波动状态在真实市场横截面中的可排序性。

### 真实数据检验

- 样本行数: `196935`
- 可用行数: `195751`
- 覆盖率: `0.9940`
- 5日 Rank IC 均值: `0.003903`
- 5日 ICIR: `0.1618`
- 五分组 Q5-Q1 均值: `0.000931`
- Top 组换手: `0.4488`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`7D Smoothed Dollar Volume Activity` is a real-data-validated framework-neutral OHLCV factor Skill in the `Liquidity` family.

### Factor Logic

```text
smooth(dollar_volume, window=7)
```

This factor combines `Dollar Volume Activity` with a `Smoothed` transform to test whether the resulting price, volume, or volatility state is cross-sectionally sortable in real market data.

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `195751`
- Coverage: `0.9940`
- 5-day Rank IC mean: `0.003903`
- 5-day ICIR: `0.1618`
- Quintile Q5-Q1 mean: `0.000931`
- Top-quintile turnover: `0.4488`
- No-lookahead check: `True`
- Status: `pass`

## License

This factor Skill is licensed under the GNU General Public License v3.0.

Copyright (C) 2026 QuantSkills.
