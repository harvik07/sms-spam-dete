"""Measure the final model on the held-out test set."""

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.pipeline import Pipeline


def evaluate(pipeline: Pipeline, texts: pd.Series, targets: pd.Series) -> dict:
    predictions = pipeline.predict(texts)
    return {
        "accuracy": accuracy_score(targets, predictions),
        "precision": precision_score(targets, predictions),
        "recall": recall_score(targets, predictions),
        "f1": f1_score(targets, predictions),
        "confusion_matrix": confusion_matrix(targets, predictions).tolist(),
    }
