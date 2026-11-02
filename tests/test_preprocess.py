from spam_detector.preprocess import clean_text, remove_stop_words, stem, tokenize


def test_tokenize_lowercases_words():
    assert tokenize("FREE Prize") == ["free", "prize"]


def test_tokenize_drops_digits_and_punctuation():
    assert tokenize("Call 0800-123, now!") == ["call", "now"]


def test_remove_stop_words():
    assert remove_stop_words(["you", "won", "the", "prize"]) == ["won", "prize"]


def test_stem_reduces_word_forms():
    assert stem(["winning", "prizes"]) == ["win", "prize"]


def test_clean_text_runs_full_chain():
    assert clean_text("You are WINNING prizes!!!") == "win prize"


def test_clean_text_handles_text_with_no_words():
    assert clean_text("123 !!!") == ""
