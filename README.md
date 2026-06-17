# 📊 skill-quant-factor-volume-stat-alpha

**简体中文** | [English](README.en.md)

> 量能、量价和统计排序类因子库：216 个独立 OHLCV 因子 Skill，真实行情验证 216/216 全部通过。

<p align="center">
  <img alt="factors" src="https://img.shields.io/badge/factors-216-brightgreen">
  <img alt="categories" src="https://img.shields.io/badge/categories-5-blue">
  <img alt="markets" src="https://img.shields.io/badge/markets-A%E8%82%A1_98%20%C2%B7%20%E7%BE%8E%E8%82%A1_50-orange">
  <img alt="sample" src="https://img.shields.io/badge/sample-2021--01--04_%E2%86%92_2026--06--10-9cf">
  <img alt="validation" src="https://img.shields.io/badge/validation-216%2F216_pass-success">
  <img alt="license" src="https://img.shields.io/badge/license-GPLv3-blue">
</p>

`skill-quant-factor-volume-stat-alpha` 是 QuantSkills 组织的量能、量价和统计排序类因子 Skill 仓库，收录用于刻画成交量、成交额、量价关系、时序排序和收益分布的 OHLCV 因子。

QuantSkills GitHub 组织：https://github.com/quantskills

这个仓库适合用于研究：

- 成交量放大和成交量标准化
- 成交额活跃度和流动性状态
- 量价相关和 OBV 斜率
- 收盘价与成交量时序排名
- 收益偏度和收益峰度

## 🧭 QuantSkills 因子库导航

QuantSkills 将这批 OHLCV 因子按研究用途拆分为三个公开 Skill 仓库：

```mermaid
flowchart LR
    D["🧭 directional-alpha<br/>方向类<br/>趋势 · 动量 · 反转 · 突破 · 通道"] ~~~ R["🛡️ risk-pattern-alpha<br/>风险与形态类<br/>波动率 · K线形态 · 震荡 · 回撤"] ~~~ V["📊 volume-stat-alpha<br/>量能与统计类（本仓库）<br/>成交量 · 量价 · 流动性 · 时序排名 · 收益分布"]

    style D fill:#e3f2fd,stroke:#1976d2
    style R fill:#ffebee,stroke:#c62828
    style V fill:#e8f5e9,stroke:#388e3c
```

- [`skill-quant-factor-directional-alpha`](https://github.com/quantskills/skill-quant-factor-directional-alpha)：方向类，包含趋势、动量、反转、突破和通道位置因子。
- [`skill-quant-factor-risk-pattern-alpha`](https://github.com/quantskills/skill-quant-factor-risk-pattern-alpha)：风险与形态类，包含波动率、K 线形态、震荡和回撤因子。
- [`skill-quant-factor-volume-stat-alpha`](https://github.com/quantskills/skill-quant-factor-volume-stat-alpha)：量能与统计类，包含成交量、量价关系、流动性、时序排名和收益分布因子。

本仓库是其中的量能与统计类因子库，不代表 QuantSkills 因子库的全部内容。

## 📦 仓库内容

本仓库包含 `216` 个因子 Skill，保留原始因子编号。

```mermaid
pie showData
    title 216 个因子的类别分布
    "Volume 成交量" : 48
    "Price Volume 量价" : 48
    "Time Series Rank 时序排名" : 48
    "Distribution 收益分布" : 48
    "Liquidity 流动性" : 24
```

| 类别 | 数量 | 说明 |
|---|---:|---|
| Volume | 48 | 成交量放大、成交量标准分 |
| Price Volume | 48 | 量价相关、OBV 斜率 |
| Liquidity | 24 | 成交额活跃度 |
| Time Series Rank | 48 | 收盘价和成交量的时序排名 |
| Distribution | 48 | 收益偏度、收益峰度 |

## 🗂️ 单个因子结构

每个因子都是一个独立 Skill 文件夹，统一放在 `factors/` 目录下，文件夹命名格式为 `<factor_id>-<english_slug>`：

```text
factors/
  R020-5d-z-scored-volume-expansion/
    SKILL.md
    README.md
    scripts/
      factor.py
      validate.py
    validation_real/
      result.json
      report.md
    references/
      formula.md
    agents/
      openai.yaml
```

## 🗃️ 数据要求

因子代码只依赖标准 OHLCV 字段：

```text
date, symbol, open, high, low, close, volume
```

推荐额外保留：

```text
market
```

## 🧪 验证口径

本仓库因子已使用真实行情面板验证：

| 验证项 | 口径 |
|---|---|
| 🇨🇳 A股 | 98 个标的 |
| 🇺🇸 美股 | 50 个标的 |
| 📅 样本区间 | 2021-01-04 到 2026-06-10 |
| ✅ 验证结果 | 216 / 216 pass |

验证指标包括覆盖率、5 日 Rank IC、5 日 ICIR、五分组 Q5-Q1 收益差、Top 组换手率和无未来函数检查。

## 🚀 使用方式

```mermaid
flowchart LR
    A["📂 进入任意因子目录<br/>factors/R020-.../"] --> B["🧪 validate.py 自检<br/>validation_real/result.json + report.md"]
    A --> C["🐍 compute_factor(df)<br/>scripts/factor.py"]
    C --> D["📈 因子值<br/>基于你自己的 OHLCV 数据"]

    style A fill:#e3f2fd,stroke:#1976d2
    style B fill:#fff3e0,stroke:#f57c00
    style D fill:#e8f5e9,stroke:#388e3c
```

进入任意因子目录后，可以直接运行自检：

```powershell
$env:PYTHONUTF8='1'
python .\scripts\validate.py
```

在代码中调用：

```python
from scripts.factor import compute_factor

result = compute_factor(df)
```

其中 `df` 是用户自己的 OHLCV 数据。

## 🗂️ 索引文件

| 文件 | 内容 |
|---|---|
| `factor_index.json` | 本仓库全部因子的元数据索引 |
| `validation_summary_real.json` | 本仓库全部因子的真实行情验证汇总 |
| `repo_summary.json` | 仓库级别统计信息 |

## 📜 License

This repository is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).

Copyright (C) 2026 QuantSkills.

## 🐼 PandaAI / QUANTSKILLS 社群

<div align="center">
  <img src="https://raw.githubusercontent.com/quantskills/.github/main/profile/assets/pandaai-community-qr.jpg" alt="PandaAI 社群二维码" width="220">
  <br>
  <sub>扫码加入 PandaAI 社群，交流 QUANTSKILLS 技能、Agent 工作流与量化研究实践。</sub>
</div>
