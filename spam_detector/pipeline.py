"""Run every stage end to end: python -m spam_detector.pipeline"""

import json

import joblib

from spam_detector import config
from spam_detector.data import add_features, load_raw, remove_duplicates, split
from spam_detector.evaluate import evaluate
from spam_detector.models import build_pipeline, candidate_models, compare_models
from spam_detector.plots import plot_confusion_matrix, plot_model_comparison


def log(stage: str, message: str) -> None:
    print(f"[{stage}] {message}", flush=True)


def run() -> dict:
    raw = load_raw()
    log("ingest", f"loaded {len(raw)} messages")

    messages = add_features(remove_duplicates(raw))
    messages = messages[messages["clean_text"] != ""]
    config.PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    messages.to_csv(config.PROCESSED_DATA_PATH, index=False)
    log("prepare", f"kept {len(messages)} unique messages")

    train, test = split(messages)
    log("split", f"{len(train)} train / {len(test)} test")

    comparison = compare_models(train["clean_text"], train["target"])
    comparison = comparison.sort_values(
        config.SELECTION_METRIC, ascending=False
    ).reset_index(drop=True)
    best_name = comparison.loc[0, "model"]
    log("compare", f"best on cross-validation: {best_name}")

    pipeline = build_pipeline(candidate_models()[best_name])
    pipeline.fit(train["clean_text"], train["target"])
    log("train", f"fitted {best_name} on the training set")

    metrics = {
        "model": best_name,
        "train_size": len(train),
        "test_size": len(test),
        **evaluate(pipeline, test["clean_text"], test["target"]),
    }
    log("evaluate", f"test f1 {metrics['f1']:.4f}")

    config.MODELS_DIR.mkdir(exist_ok=True)
    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, config.MODEL_PATH)
    config.METRICS_PATH.write_text(json.dumps(metrics, indent=2) + "\n")
    comparison.to_csv(config.COMPARISON_PATH, index=False)
    plot_model_comparison(comparison, config.FIGURES_DIR / "model_comparison.png")
    plot_confusion_matrix(
        metrics["confusion_matrix"], config.FIGURES_DIR / "confusion_matrix.png"
    )
    log("report", f"saved artifacts to {config.MODELS_DIR.name}/ and reports/")
    return metrics


if __name__ == "__main__":
    run()
