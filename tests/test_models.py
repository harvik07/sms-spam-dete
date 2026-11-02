from conftest import SAMPLE_MESSAGES

import pandas as pd

from spam_detector.models import candidate_models, compare_models
from spam_detector.preprocess import clean_text


def test_candidates_cover_six_models():
    assert len(candidate_models()) == 6


def test_compare_models_returns_a_row_per_candidate():
    sample = SAMPLE_MESSAGES * 4
    texts = pd.Series([clean_text(text) for text, _ in sample])
    targets = pd.Series([target for _, target in sample])
    comparison = compare_models(texts, targets, folds=2)
    assert len(comparison) == 6
    assert comparison["f1"].between(0, 1).all()
