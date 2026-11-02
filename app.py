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
