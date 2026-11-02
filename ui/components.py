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


def highlight(text: str, signals: dict[str, float]) -> str:
    """Escape the message and mark words that pushed the score up or down."""

    def mark(match: re.Match) -> str:
        word = match.group(0)
        weight = signals.get(clean_text(word), 0)
        if weight >= MIN_SIGNAL:
            return f'<mark class="up">{html.escape(word)}</mark>'
        if weight <= -MIN_SIGNAL:
            return f'<mark class="down">{html.escape(word)}</mark>'
        return html.escape(word)

    return "".join(mark(part) for part in re.finditer(r"[A-Za-z]+|[^A-Za-z]+", text))
