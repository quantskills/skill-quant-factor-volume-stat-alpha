from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd


def load_module():
    path = Path(__file__).resolve().parent / "factor.py"
    spec = importlib.util.spec_from_file_location("factor_module", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_sample() -> pd.DataFrame:
    rng = np.random.default_rng(11)
    rows = []
    dates = pd.date_range("2023-01-01", periods=180, freq="B")
    for i in range(12):
        close = 50 * np.exp(np.cumsum(rng.normal(0.0002, 0.018, len(dates))))
        open_ = np.r_[close[0], close[:-1]] * (1 + rng.normal(0, 0.004, len(dates)))
        high = np.maximum(open_, close) * (1 + rng.uniform(0.001, 0.02, len(dates)))
        low = np.minimum(open_, close) * (1 - rng.uniform(0.001, 0.02, len(dates)))
        volume = rng.integers(100000, 3000000, len(dates))
        for j, date in enumerate(dates):
            rows.append({"date": date, "symbol": f"S{i:03d}", "open": open_[j], "high": high[j], "low": low[j], "close": close[j], "volume": volume[j]})
    return pd.DataFrame(rows)


def main() -> int:
    module = load_module()
    result = module.generate_signals(make_sample())
    col = module.FACTOR_COLUMN
    required = {col, "signal", "position", "long_entry", "short_entry", "exit_long", "exit_short"}
    missing = required.difference(result.columns)
    if missing:
        raise AssertionError(f"missing output columns: {sorted(missing)}")
    finite = int(np.isfinite(result[col].replace([np.inf, -np.inf], np.nan).dropna()).sum())
    if finite <= 0:
        raise AssertionError("factor produced no finite values")
    print(json.dumps({"status": "ok", "factor": col, "rows": len(result), "finite": finite}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
