import matplotlib.pyplot as plt

def save_dashboard(equity, drawdown, returns, signal):
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    axes[0, 0].plot(equity)
    axes[0, 0].set_title("Equity")

    axes[0, 1].plot(drawdown)
    axes[0, 1].set_title("Drawdown")

    axes[1, 0].hist(returns, bins=80)
    axes[1, 0].set_title("Returns")

    axes[1, 1].plot(signal)
    axes[1, 1].set_title("Signal")

    plt.tight_layout()
    plt.savefig("charts/dashboard.png", dpi=150)
    plt.close()
