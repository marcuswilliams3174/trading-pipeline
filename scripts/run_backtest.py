import numpy as np
import pandas as pd

def run_backtest(df):
    df = df.copy()

    # -------------------------
    # CLEAN INPUTS
    # -------------------------
    df["signal"] = df["signal"].fillna(0)
    df["position"] = df["position"].clip(-1, 1)

    # -------------------------
    # STRATEGY PNL
    # -------------------------
    df["strategy_pnl"] = df["position"] * df["book_pnl"]

    # normalize
    scale = df["strategy_pnl"].abs().quantile(0.95)
    df["strategy_ret"] = df["strategy_pnl"] / (10 * scale)
    df["strategy_ret"] *= 0.05

    # -------------------------
    # EQUITY
    # -------------------------
    equity = (1 + df["strategy_ret"]).cumprod()

    return df, equity
