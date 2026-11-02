from streamlit.testing.v1 import AppTest


def run_app() -> AppTest:
    return AppTest.from_file("app.py", default_timeout=30).run()


def inspect_button(app: AppTest):
    return next(b for b in app.button if b.label == "Inspect message")


def test_app_starts_cleanly():
    assert not run_app().exception


def test_flags_spam_message():
    app = run_app()
    app.text_area(key="message").set_value(
        "URGENT! You have won a guaranteed cash prize. Call now to claim."
    )
    inspect_button(app).click().run()
    assert not app.exception
    assert any("SPAM" in block.value and "stamp" in block.value for block in app.markdown)


def test_warns_on_empty_message():
    app = run_app()
    inspect_button(app).click().run()
    assert app.warning[0].value == "Paste a message first."
