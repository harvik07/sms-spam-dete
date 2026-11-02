"""Score new messages with the trained pipeline."""

from dataclasses import dataclass
from pathlib import Path

import joblib
from scipy.special import expit
from sklearn.pipeline import Pipeline

from spam_detector.config import MODEL_PATH
from spam_detector.preprocess import clean_text

SPAM_THRESHOLD = 0.5


@dataclass(frozen=True)
class Prediction:
    is_spam: bool
    spam_score: float
    signals: dict[str, float]


class SpamDetector:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    @classmethod
    def load(cls, path: Path = MODEL_PATH) -> "SpamDetector":
        return cls(joblib.load(path))

    def _scores(self, cleaned: list[str]) -> list[float]:
        """Spam score in 0-1, for models with or without predict_proba."""
        if hasattr(self.pipeline, "predict_proba"):
            return self.pipeline.predict_proba(cleaned)[:, 1].tolist()
        return expit(self.pipeline.decision_function(cleaned)).tolist()
