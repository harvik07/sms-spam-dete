from ui.components import highlight


def test_highlight_escapes_html():
    assert "<script>" not in highlight("<script>alert(1)</script>", {})


def test_highlight_marks_spam_words():
    assert '<mark class="up">Prize</mark>' in highlight("Prize", {"prize": 0.3})


def test_highlight_marks_safe_words():
    assert '<mark class="down">home</mark>' in highlight("home", {"home": -0.3})


def test_highlight_keeps_weak_words_plain():
    assert highlight("hello", {"hello": 0.001}) == "hello"
