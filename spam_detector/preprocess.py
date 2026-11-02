"""Turn raw SMS text into normalized tokens."""

import re

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

_WORD_PATTERN = re.compile(r"[a-z]+")
_stemmer = PorterStemmer()


def tokenize(text: str) -> list[str]:
    """Lowercase the text and keep alphabetic words only."""
    return _WORD_PATTERN.findall(text.lower())


def remove_stop_words(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in ENGLISH_STOP_WORDS]
