import pytest


def test_flags_spam(detector):
    assert detector.predict("Claim your free cash prize now").is_spam


def test_passes_normal_message(detector):
    assert not detector.predict("Lunch at home tomorrow afternoon").is_spam


def test_score_is_a_probability(detector):
    assert 0 <= detector.predict("Win cash").spam_score <= 1


def test_signals_point_at_spam_words(detector):
    signals = detector.predict("Claim your free prize").signals
    assert signals["prize"] > 0


def test_rejects_empty_message(detector):
    with pytest.raises(ValueError):
        detector.predict("   ")


def test_message_with_no_words_has_no_signals(detector):
    assert detector.predict("123 !!!").signals == {}
