import pandas as pd

from spam_detector.data import add_features, load_raw, remove_duplicates, split


def test_load_raw_reads_every_message():
    df = load_raw()
    assert len(df) == 5574
    assert set(df["label"]) == {"ham", "spam"}


def test_remove_duplicates_keeps_first_copy():
    df = pd.DataFrame({"label": ["ham", "ham"], "text": ["hi", "hi"]})
    assert len(remove_duplicates(df)) == 1


def test_add_features_maps_labels():
    df = pd.DataFrame({"label": ["ham", "spam"], "text": ["hello", "win prize"]})
    assert add_features(df)["target"].tolist() == [0, 1]


def test_split_preserves_spam_ratio():
    train, test = split(add_features(remove_duplicates(load_raw())))
    assert abs(train["target"].mean() - test["target"].mean()) < 0.01
    assert not set(train["text"]) & set(test["text"])
