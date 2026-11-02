"""Candidate models. Every estimator runs with its library default settings."""

import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from spam_detector.config import CV_FOLDS, RANDOM_STATE

SCORING = ["accuracy", "precision", "recall", "f1"]


def candidate_models() -> dict[str, BaseEstimator]:
    return {
        "Naive Bayes": MultinomialNB(),
        "Logistic Regression": LogisticRegression(random_state=RANDOM_STATE),
        "Support Vector Machine": SVC(random_state=RANDOM_STATE),
        "Random Forest": RandomForestClassifier(random_state=RANDOM_STATE),
        "Decision Tree": DecisionTreeClassifier(random_state=RANDOM_STATE),
        "K-Nearest Neighbors": KNeighborsClassifier(),
    }


def build_pipeline(estimator: BaseEstimator) -> Pipeline:
    """Keep TF-IDF inside the pipeline so it only ever learns from training folds."""
    return Pipeline([("tfidf", TfidfVectorizer()), ("model", estimator)])


def compare_models(
    texts: pd.Series, targets: pd.Series, folds: int = CV_FOLDS
) -> pd.DataFrame:
    """Cross-validate every candidate and return one row per model."""
    splitter = StratifiedKFold(n_splits=folds, shuffle=True, random_state=RANDOM_STATE)
    rows = []
    for name, estimator in candidate_models().items():
        scores = cross_validate(
            build_pipeline(estimator), texts, targets, cv=splitter, scoring=SCORING
        )
        row = {"model": name}
        row.update({metric: scores[f"test_{metric}"].mean() for metric in SCORING})
        rows.append(row)
    return pd.DataFrame(rows)
