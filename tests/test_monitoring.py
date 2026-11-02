from prometheus_client import REGISTRY

from spam_detector import monitoring


def sample(name: str, labels: dict) -> float:
    return REGISTRY.get_sample_value(name, labels) or 0


def test_records_request_and_verdict(detector):
    requests = sample("spam_requests_total", {"source": "single"})
    spam = sample("spam_predictions_total", {"verdict": "spam"})
    monitoring.predict_and_record(detector, "Claim your free cash prize", "single")
    assert sample("spam_requests_total", {"source": "single"}) == requests + 1
    assert sample("spam_predictions_total", {"verdict": "spam"}) == spam + 1


def test_publishes_offline_scores(monkeypatch):
    monkeypatch.setattr(monitoring, "_server_started", True)
    scores = {"accuracy": 0.9, "precision": 0.8, "recall": 0.7, "f1": 0.75}
    monitoring.start_server({"model": "Test model", **scores})
    assert sample("spam_model_test_score", {"metric": "accuracy"}) == 0.9
    assert sample("spam_model_info", {"model": "Test model"}) == 1
