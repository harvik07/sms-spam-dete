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

    def _signals(self, cleaned: str, base_score: float) -> dict[str, float]:
        """How much the score drops when each word is left out."""
        tokens = cleaned.split()
        unique = list(dict.fromkeys(tokens))
        without = [" ".join(t for t in tokens if t != word) for word in unique]
        return {
            word: base_score - score
            for word, score in zip(unique, self._scores(without))
        }

    def predict(self, text: str) -> Prediction:
        if not text.strip():
            raise ValueError("Message is empty")
        cleaned = clean_text(text)
        score = self._scores([cleaned])[0]
        signals = self._signals(cleaned, score) if cleaned else {}
        return Prediction(score >= SPAM_THRESHOLD, score, signals)
