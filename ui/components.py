"""HTML fragments used by the Streamlit app. All message text is escaped."""

import html
import re

from spam_detector.predict import Prediction
from spam_detector.preprocess import clean_text

MIN_SIGNAL = 0.01


def masthead() -> str:
    return """
    <div class="masthead">
      <div class="kicker">Message inspection desk</div>
      <h1>Is this text spam?</h1>
      <p>Paste an SMS and see the verdict, plus the words that drove it.</p>
    </div>
    """
