"""Load the UCI SMS Spam Collection and prepare it for modelling."""

import csv
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from spam_detector.config import RANDOM_STATE, RAW_DATA_PATH, TEST_SIZE
from spam_detector.preprocess import clean_text

LABELS = {"ham": 0, "spam": 1}


def load_raw(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Read the tab-separated dataset. Messages contain stray quotes, so quoting is off."""
    return pd.read_csv(
        path,
        sep="\t",
        header=None,
        names=["label", "text"],
        quoting=csv.QUOTE_NONE,
        encoding="latin-1",
    )


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop repeated messages so one cannot land in both train and test."""
    return df.drop_duplicates(subset="text", keep="first").reset_index(drop=True)
