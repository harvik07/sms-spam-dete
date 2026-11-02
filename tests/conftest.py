import pytest
from sklearn.naive_bayes import MultinomialNB

from spam_detector.models import build_pipeline
from spam_detector.predict import SpamDetector
from spam_detector.preprocess import clean_text

SAMPLE_MESSAGES = [
    ("Win a free prize now, call to claim your cash", 1),
    ("Free entry to win cash, claim your prize today", 1),
    ("Urgent! You won a free holiday, call now", 1),
    ("Are we still having lunch tomorrow", 0),
    ("Can you pick up milk on your way home", 0),
    ("See you at the meeting this afternoon", 0),
]


@pytest.fixture(scope="session")
def detector() -> SpamDetector:
    texts = [clean_text(text) for text, _ in SAMPLE_MESSAGES]
    targets = [target for _, target in SAMPLE_MESSAGES]
    return SpamDetector(build_pipeline(MultinomialNB()).fit(texts, targets))
