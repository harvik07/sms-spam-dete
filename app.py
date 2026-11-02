import json

import pandas as pd
import streamlit as st

from spam_detector.config import COMPARISON_PATH, FIGURES_DIR, METRICS_PATH
from spam_detector.predict import SpamDetector
from ui import components
from ui.theme import CSS

EXAMPLES = {
    "Prize scam": "URGENT! You have won a guaranteed cash prize. Call now to claim your reward.",
    "Friend": "Hey, are we still on for dinner tonight? I can pick you up around 7.",
    "Bank alert": "Your account has been selected for a free loan offer. Reply YES to claim.",
}


@st.cache_resource
def load_detector() -> SpamDetector:
    return SpamDetector.load()


@st.cache_data
def load_metrics() -> dict:
    return json.loads(METRICS_PATH.read_text())


def use_example(text: str) -> None:
    st.session_state["message"] = text


def render_inspect(detector: SpamDetector) -> None:
    st.text_area(
        "Message",
        key="message",
        height=130,
        placeholder="Paste a text message here",
    )

    st.caption("Or try an example")
    for column, (label, text) in zip(st.columns(len(EXAMPLES)), EXAMPLES.items()):
        column.button(
            label, on_click=use_example, args=(text,), width="stretch"
        )

    if st.button("Inspect message", type="primary", width="stretch"):
        message = st.session_state["message"]
        if not message.strip():
            st.warning("Paste a message first.")
            return
        prediction = detector.predict(message)
        st.markdown(
            components.verdict_card(message, prediction), unsafe_allow_html=True
        )
        if not prediction.signals:
            st.info("No recognizable words here, so this verdict is a weak guess.")
