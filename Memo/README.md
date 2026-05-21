# Systematic Trading Research Platform

End-to-end quantitative trading framework for transforming raw market signals into a fully risk-adjusted portfolio simulation and performance analytics pipeline.

---

## Overview

This project implements a modular systematic trading workflow:

Signal Generation → Position Sizing → Strategy PnL → Risk Normalization → Strategy Returns → Equity Curve

The framework was designed to separate alpha generation, portfolio construction, risk management, and visualization into independent modules similar to institutional quantitative research pipelines.

---

## Core Features

### Signal Engine
- Continuous signal generation framework
- Bounded exposure logic
- Modular signal architecture

### Portfolio Construction
- Position sizing and exposure control
- Vectorized backtesting pipeline
- Stable return construction

### Risk Management
- Volatility normalization
- Return scaling for compounding stability
- Drawdown-aware diagnostics

### Performance Analytics
- Equity curve construction
- Drawdown analysis
- Return distribution diagnostics
- Dashboard visualization



Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit

Key Design Principle

Raw PnL should not be compounded directly.

The framework normalizes strategy PnL into stable return series before equity construction to avoid leverage distortion and unstable compounding behavior.

Example Outputs
- Log equity curve
- Drawdown profile
- Return distribution
- Signal diagnostics dashboard

Future Improvements
- Sharpe / Sortino analytics
- Multi-asset portfolio support
- Transaction cost modeling
- Walk-forward validation
- Regime-aware allocation
- Live dashboard deployment

Running the Dashboard
streamlit run streamlit_app.py

---

## Repository Structure

```text
trading-pipeline/
│
├── charts/          # saved dashboard outputs
├── notebooks/       # research notebooks
├── scripts/         # execution + utility scripts
├── src/             # core trading logic
├── visuals/         # dashboard visualization
│
├── README.md
├── requirements.txt
└── streamlit_app.py
