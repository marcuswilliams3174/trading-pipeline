import numpy as np

def normalize_returns(pnl):
    scale = pnl.abs().quantile(0.95)
    return pnl / (10 * scale)
