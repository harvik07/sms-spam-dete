"""Paths and constants shared across the project."""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_PATH = ROOT_DIR / "data" / "raw" / "SMSSpamCollection"
PROCESSED_DATA_PATH = ROOT_DIR / "data" / "processed" / "messages.csv"

MODELS_DIR = ROOT_DIR / "models"
MODEL_PATH = MODELS_DIR / "spam_pipeline.joblib"
METRICS_PATH = MODELS_DIR / "metrics.json"

REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
COMPARISON_PATH = REPORTS_DIR / "model_comparison.csv"
