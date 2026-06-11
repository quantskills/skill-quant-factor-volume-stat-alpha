from __future__ import annotations

import numpy as np
import pandas as pd

SPEC = {
  "factor_id": "R584",
  "slug": "10d-delta-price-volume-correlation",
  "name_cn": "10日变化量价相关",
  "name_en": "10D Delta Price Volume Correlation",
  "category_cn": "量价",
  "category_en": "Price Volume",
  "base": "price_volume_corr",
  "transform": "delta",
  "params": {
    "window": 10,
    "norm": 20,
    "lag": 2,
    "smooth": 3,
    "skip": 5,
    "fast": 3,
    "slow": 10
  },
  "formula_cn": "delta(price_volume_corr, window=10)",
  "formula_en": "delta(price_volume_corr, window=10)",
  "rationale_cn": "该因子把“量价相关”与“变化”处理结合，用来刻画价格、量能或波动状态在横截面上的可排序性。",
  "rationale_en": "This factor combines Price Volume Correlation with a Delta transform to test cross-sectional sortability in price, volume, or volatility states."
}
FACTOR_COLUMN = SPEC["slug"]
REQUIRED_COLUMNS = ("open", "high", "low", "close", "volume")


def _minp(window: int, floor: int = 5) -> int:
    return min(window, max(2, min(floor, window // 2 if window > 2 else 2)))


def _zscore(series: pd.Series, window: int) -> pd.Series:
    mean = series.rolling(window, min_periods=_minp(window)).mean()
    std = series.rolling(window, min_periods=_minp(window)).std(ddof=0)
    return (series - mean) / std.replace(0, np.nan)


def _ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False, min_periods=_minp(span, 3)).mean()


def _atr(data: pd.DataFrame, window: int) -> pd.Series:
    high = data["high"]
    low = data["low"]
    close = data["close"]
    prev = close.shift(1)
    tr = pd.concat([(high - low), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(window, min_periods=_minp(window)).mean()


def _rsi(close: pd.Series, window: int) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1.0 / window, adjust=False, min_periods=_minp(window)).mean()
    avg_loss = loss.ewm(alpha=1.0 / window, adjust=False, min_periods=_minp(window)).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _rolling_slope(series: pd.Series, window: int) -> pd.Series:
    window = max(3, int(window))
    x = np.arange(window, dtype=float)
    x = x - x.mean()
    denom = float(np.sum(x * x))
    def calc(values: np.ndarray) -> float:
        if np.isnan(values).any():
            return np.nan
        y = values - values.mean()
        return float(np.sum(x * y) / denom)
    return series.rolling(window, min_periods=window).apply(calc, raw=True)


def _ts_rank(series: pd.Series, window: int) -> pd.Series:
    def calc(values: np.ndarray) -> float:
        valid = values[~np.isnan(values)]
        if len(valid) == 0:
            return np.nan
        return float(pd.Series(valid).rank(pct=True).iloc[-1])
    return series.rolling(window, min_periods=_minp(window)).apply(calc, raw=True)


def _base(data: pd.DataFrame) -> pd.Series:
    params = SPEC["params"]
    base = SPEC["base"]
    close = data["close"].astype(float)
    open_ = data["open"].astype(float)
    high = data["high"].astype(float)
    low = data["low"].astype(float)
    volume = data["volume"].astype(float)
    ret = close.pct_change()
    w = int(params.get("window", 20))
    fast = int(params.get("fast", max(3, w // 3)))
    slow = int(params.get("slow", w))
    if base == "return": return close.pct_change(w)
    if base == "skip_return": return close.shift(int(params.get("skip", 5))).pct_change(w)
    if base == "reversal": return -close.pct_change(w)
    if base == "sma_gap": return close / close.rolling(w, min_periods=_minp(w)).mean() - 1
    if base == "ema_gap": return close / _ema(close, w) - 1
    if base == "dual_ema_gap": return (_ema(close, fast) - _ema(close, slow)) / close.replace(0, np.nan)
    if base == "sma_slope": return _rolling_slope(close.rolling(w, min_periods=_minp(w)).mean(), min(30, max(5, w // 2))) / close.replace(0, np.nan)
    if base == "range_position":
        lo = low.rolling(w, min_periods=_minp(w)).min(); hi = high.rolling(w, min_periods=_minp(w)).max()
        return (close - lo) / (hi - lo).replace(0, np.nan) - 0.5
    if base == "breakout": return close / high.shift(1).rolling(w, min_periods=_minp(w)).max().replace(0, np.nan) - 1
    if base == "breakdown": return -(close / low.shift(1).rolling(w, min_periods=_minp(w)).min().replace(0, np.nan) - 1)
    if base == "rsi": return _rsi(close, w) / 100 - 0.5
    if base == "rsi_reversal": return 0.5 - _rsi(close, w) / 100
    if base == "stoch":
        lo = low.rolling(w, min_periods=_minp(w)).min(); hi = high.rolling(w, min_periods=_minp(w)).max()
        return (close - lo) / (hi - lo).replace(0, np.nan) - 0.5
    if base == "atr_ratio": return _atr(data, w) / close.replace(0, np.nan)
    if base == "range_ratio": return ((high - low) / close.replace(0, np.nan)).rolling(w, min_periods=_minp(w)).mean()
    if base == "realized_vol": return ret.rolling(w, min_periods=_minp(w)).std(ddof=0)
    if base == "downside_vol": return ret.where(ret < 0, 0).rolling(w, min_periods=_minp(w)).std(ddof=0)
    if base == "trend_strength": return close.pct_change(w) / ret.rolling(w, min_periods=_minp(w)).std(ddof=0).replace(0, np.nan)
    if base == "efficiency":
        return (close - close.shift(w)).abs() / close.diff().abs().rolling(w, min_periods=_minp(w)).sum().replace(0, np.nan)
    if base == "volume_ratio": return volume / volume.rolling(w, min_periods=_minp(w)).mean() - 1
    if base == "volume_z": return _zscore(volume, w)
    if base == "dollar_volume":
        dollar = close * volume
        return dollar / dollar.rolling(w, min_periods=_minp(w)).mean() - 1
    if base == "price_volume_corr": return ret.rolling(w, min_periods=_minp(w)).corr(volume.pct_change())
    if base == "obv_slope":
        obv = (np.sign(close.diff()).fillna(0) * volume).cumsum()
        return _rolling_slope(obv, min(w, 60)) / volume.rolling(w, min_periods=_minp(w)).mean().replace(0, np.nan)
    if base == "gap_sum": return (open_ / close.shift(1) - 1).rolling(w, min_periods=_minp(w)).sum()
    if base == "intraday": return (close / open_.replace(0, np.nan) - 1).rolling(w, min_periods=_minp(w)).mean()
    if base == "upper_wick":
        top = pd.concat([open_, close], axis=1).max(axis=1)
        return ((high - top) / (high - low).replace(0, np.nan)).rolling(w, min_periods=_minp(w)).mean()
    if base == "lower_wick":
        bottom = pd.concat([open_, close], axis=1).min(axis=1)
        return ((bottom - low) / (high - low).replace(0, np.nan)).rolling(w, min_periods=_minp(w)).mean()
    if base == "drawdown": return close / close.rolling(w, min_periods=_minp(w)).max().replace(0, np.nan) - 1
    if base == "ts_rank_close": return _ts_rank(close, w) - 0.5
    if base == "ts_rank_volume": return _ts_rank(volume, w) - 0.5
    if base == "ret_skew": return ret.rolling(w, min_periods=_minp(w, 10)).skew()
    if base == "ret_kurt": return ret.rolling(w, min_periods=_minp(w, 10)).kurt()
    raise ValueError(f"unknown base: {base}")


def _transform(signal: pd.Series, data: pd.DataFrame) -> pd.Series:
    params = SPEC["params"]
    transform = SPEC["transform"]
    w = int(params.get("window", 20))
    norm = int(params.get("norm", max(20, w)))
    ret = data["close"].pct_change()
    if transform == "raw": return signal
    if transform == "neg": return -signal
    if transform == "z": return _zscore(signal, norm)
    if transform == "delta": return signal - signal.shift(int(params.get("lag", max(1, w // 4))))
    if transform == "smooth": return _ema(signal, int(params.get("smooth", max(3, w // 3))))
    if transform == "rank": return _ts_rank(signal, norm) - 0.5
    if transform == "vol_scaled":
        vol = ret.rolling(norm, min_periods=_minp(norm)).std(ddof=0)
        return signal / vol.replace(0, np.nan)
    if transform == "stability":
        vol = signal.rolling(norm, min_periods=_minp(norm)).std(ddof=0)
        return signal / vol.replace(0, np.nan)
    if transform == "confirm_volume":
        volume = data["volume"].astype(float)
        return signal * (volume / volume.rolling(norm, min_periods=_minp(norm)).mean())
    if transform == "compress": return np.tanh(signal)
    raise ValueError(f"unknown transform: {transform}")


def compute_factor(df: pd.DataFrame, **params) -> pd.DataFrame:
    data = df.copy()
    data.columns = [str(c).lower() for c in data.columns]
    missing = [c for c in REQUIRED_COLUMNS if c not in data.columns]
    if missing:
        raise ValueError(f"missing required OHLCV columns: {missing}")
    if "symbol" not in data.columns: data["symbol"] = "asset"
    if "date" not in data.columns: data["date"] = pd.RangeIndex(len(data))
    data = data.sort_values(["symbol", "date"]).reset_index(drop=True)
    values = []
    for _, group in data.groupby("symbol", sort=False):
        values.append(_transform(_base(group), group))
    data[FACTOR_COLUMN] = pd.concat(values).sort_index()
    return data


def generate_signals(df: pd.DataFrame, quantile: float = 0.8, **params) -> pd.DataFrame:
    out = compute_factor(df, **params)
    out["factor_rank"] = out.groupby("date")[FACTOR_COLUMN].rank(pct=True)
    out["long_entry"] = out["factor_rank"] >= quantile
    out["short_entry"] = out["factor_rank"] <= (1 - quantile)
    out["signal"] = np.select([out["long_entry"], out["short_entry"]], [1, -1], default=0)
    out["position"] = out["signal"]
    out["exit_long"] = out["signal"] <= 0
    out["exit_short"] = out["signal"] >= 0
    out["action"] = np.select([out["long_entry"], out["short_entry"]], ["buy", "sellshort"], default="")
    return out
