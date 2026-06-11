# 5日标准化成交量标准分

中文 | [English](#english)

## 中文

`5日标准化成交量标准分` 是一个使用真实行情验证过的 OHLCV 因子 Skill，属于 `量能` 类。

### 因子逻辑

```text
z(volume_z, window=5)
```

该因子将 `成交量标准分` 与 `标准化` 处理结合，观察价格、量能或波动状态在真实市场横截面中的可排序性。

### 真实数据检验

- 样本行数: `196935`
- 可用行数: `195455`
- 覆盖率: `0.9925`
- 5日 Rank IC 均值: `0.001448`
- 5日 ICIR: `0.0644`
- 五分组 Q5-Q1 均值: `0.000384`
- Top 组换手: `0.7442`
- 无未来函数检查: `True`
- 状态: `pass`

详细结果见 `validation_real/report.md` 和 `validation_real/result.json`。

## QuantSkills Collection

This factor is part of the QuantSkills `skill-quant-factor-volume-stat-alpha` factor library. QuantSkills publishes three related OHLCV factor libraries: `skill-quant-factor-directional-alpha`, `skill-quant-factor-risk-pattern-alpha`, and `skill-quant-factor-volume-stat-alpha`. Choose the library that matches the research objective.

## English

`5D Z-Scored Volume Z-Score` is a real-data-validated framework-neutral OHLCV factor Skill in the `Volume` family.

### Factor Logic

```text
z(volume_z, window=5)
```

This factor combines `Volume Z-Score` with a `Z-Scored` transform to test whether the resulting price, volume, or volatility state is cross-sectionally sortable in real market data.

### Real-Data Validation

- Sample rows: `196935`
- Usable rows: `195455`
- Coverage: `0.9925`
- 5-day Rank IC mean: `0.001448`
- 5-day ICIR: `0.0644`
- Quintile Q5-Q1 mean: `0.000384`
- Top-quintile turnover: `0.7442`
- No-lookahead check: `True`
- Status: `pass`

## License

This factor Skill is licensed under the GNU General Public License v3.0.

Copyright (C) 2026 QuantSkills.
