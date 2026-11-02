"""Charts saved next to the training report."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

INK = "#1f2a37"
ACCENT = "#c2410c"
MUTED = "#c9c3b6"


def plot_model_comparison(comparison: pd.DataFrame, path: Path) -> None:
    ordered = comparison.sort_values("f1")
    colors = [MUTED] * (len(ordered) - 1) + [ACCENT]
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.barh(ordered["model"], ordered["f1"], color=colors)
    ax.bar_label(bars, fmt="%.3f", padding=4, color=INK)
    ax.set_xlim(0, 1.08)
    ax.set_xlabel("Mean cross-validated F1")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
