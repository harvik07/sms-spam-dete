"""Prometheus metrics for the running app."""

import os
from time import perf_counter

from prometheus_client import Counter, Gauge, Histogram, start_http_server

from spam_detector.predict import Prediction, SpamDetector

METRICS_PORT = int(os.environ.get("METRICS_PORT", "9100"))
OFFLINE_METRICS = ("accuracy", "precision", "recall", "f1")

REQUESTS = Counter(
    "spam_requests_total", "Messages inspected", ["source"]
)
PREDICTIONS = Counter(
    "spam_predictions_total", "Verdicts returned", ["verdict"]
)
REJECTED = Counter(
    "spam_rejected_requests_total", "Empty submissions that were not scored"
)
LATENCY = Histogram(
    "spam_prediction_latency_seconds",
    "Time to score one message",
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5),
)
SCORES = Histogram(
    "spam_score",
    "Spam score of inspected messages",
    buckets=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),
)
MESSAGE_LENGTH = Histogram(
    "spam_message_length_characters",
    "Length of inspected messages",
    buckets=(20, 50, 100, 160, 320, 640, 1280),
)
MODEL_TEST_SCORE = Gauge(
    "spam_model_test_score", "Score on the held-out test set at training time", ["metric"]
)
MODEL_INFO = Gauge("spam_model_info", "Model currently loaded", ["model"])

_server_started = False


def start_server(metrics: dict) -> None:
    """Publish the offline scores and serve /metrics once per process."""
    global _server_started
    for name in OFFLINE_METRICS:
        MODEL_TEST_SCORE.labels(metric=name).set(metrics[name])
    MODEL_INFO.labels(model=metrics["model"]).set(1)
    if _server_started:
        return
    try:
        start_http_server(METRICS_PORT)
    except OSError as error:
        print(f"Metrics server not started on port {METRICS_PORT}: {error}", flush=True)
    _server_started = True


def predict_and_record(detector: SpamDetector, text: str, source: str) -> Prediction:
    started = perf_counter()
    prediction = detector.predict(text)
    LATENCY.observe(perf_counter() - started)
    REQUESTS.labels(source=source).inc()
    PREDICTIONS.labels(verdict="spam" if prediction.is_spam else "clean").inc()
    SCORES.observe(prediction.spam_score)
    MESSAGE_LENGTH.observe(len(text))
    return prediction
