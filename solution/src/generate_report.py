"""Generate a simple Evidently report from recent API requests."""

from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


ROOT_DIR = Path(__file__).resolve().parents[1]
REFERENCE_DATA_PATH = ROOT_DIR / "data" / "raw" / "iris.csv"
REQUEST_LOG_PATH = ROOT_DIR / "monitoring" / "requests.csv"
REPORT_PATH = ROOT_DIR / "monitoring" / "reports" / "data_drift_report.html"

FEATURE_COLUMNS = [
    "sepal_length_cm",
    "sepal_width_cm",
    "petal_length_cm",
    "petal_width_cm",
]


def generate_report() -> Path:
    """Compare reference training data with recent request data."""
    if not REQUEST_LOG_PATH.exists():
        raise FileNotFoundError(
            "The request log is missing. Send a few requests to the API before "
            "running the Evidently report."
        )

    reference_data = pd.read_csv(REFERENCE_DATA_PATH)[FEATURE_COLUMNS]
    current_data = pd.read_csv(REQUEST_LOG_PATH)[FEATURE_COLUMNS]

    if current_data.empty:
        raise ValueError(
            "The request log is empty. Send at least one prediction request first."
        )
    if len(current_data) < 5:
        raise ValueError(
            "The request log is too small for a useful report. Send at least five "
            "prediction requests first."
        )

    report = Report(metrics=[DataDriftPreset()])
    snapshot = report.run(reference_data=reference_data, current_data=current_data)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    snapshot.save_html(str(REPORT_PATH))
    return REPORT_PATH


if __name__ == "__main__":
    output_path = generate_report()
    print(f"Wrote Evidently report to {output_path}")
