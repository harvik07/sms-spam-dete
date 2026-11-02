"""Container entrypoint: expose /metrics before the first browser session.

Streamlit only runs app.py when someone opens the page, so the metrics server
has to start here for Prometheus to reach the app from the moment it boots.
"""

import json
import sys

from streamlit.web import cli

from spam_detector import monitoring
from spam_detector.config import METRICS_PATH, ROOT_DIR


def main() -> None:
    monitoring.start_server(json.loads(METRICS_PATH.read_text()))
    sys.argv = ["streamlit", "run", str(ROOT_DIR / "app.py"), *sys.argv[1:]]
    cli.main()


if __name__ == "__main__":
    main()
