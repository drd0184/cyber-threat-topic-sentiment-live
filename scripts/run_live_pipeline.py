"""
Run the operational live pipeline.

This orchestrator is intended for a 12-hour operational run from Windows Task
Scheduler or GitHub Actions. It does not retrain LDA, does not modify dashboard
UI files, and does not delete raw data. The official live LDA model is used
only for topic assignment.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil
import subprocess
import sys
import time


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "logs" / "live_pipeline"

PIPELINE_STEPS = [
    ("Collect live sources", "scripts/00_collect_live_sources.py"),
    ("Inspect live raw dataset", "scripts/00b_inspect_live_dataset.py"),
    ("Prepare social/news dataset", "scripts/01_prepare_live_social_news_dataset.py"),
    ("Filter noise", "scripts/02_live_filter_noise.py"),
    ("Preprocess text", "scripts/03_live_preprocess_text.py"),
    ("Assign topics with official live LDA", "scripts/04_live_assign_topics_existing_live_lda.py"),
    ("Apply official live topic labels", "scripts/04c_apply_live_topic_labels.py"),
    ("Run VADER sentiment", "scripts/05_live_sentiment_vader.py"),
    ("Aggregate temporal windows", "scripts/06_live_temporal_aggregation.py"),
    ("Compute live P2 index", "scripts/07_live_compute_p2_index.py"),
]

LIVE_DASHBOARD_EXPORT_SCRIPT = PROJECT_ROOT / "scripts" / "11_export_live_dashboard_data.py"
if LIVE_DASHBOARD_EXPORT_SCRIPT.exists():
    PIPELINE_STEPS.append(("Export live dashboard data", "scripts/11_export_live_dashboard_data.py"))
# TODO: Keep dashboard UI changes outside the scheduled pipeline.


class TeeLogger:
    def __init__(self, log_path: Path) -> None:
        self.log_path = log_path
        self.log_file = log_path.open("w", encoding="utf-8", newline="")

    def write(self, message: str) -> None:
        print(message, end="")
        self.log_file.write(message)
        self.log_file.flush()

    def line(self, message: str = "") -> None:
        self.write(message + "\n")

    def close(self) -> None:
        self.log_file.close()


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def run_step(step_number: int, total_steps: int, name: str, script_path: str, logger: TeeLogger) -> int:
    absolute_script_path = PROJECT_ROOT / script_path
    command = [sys.executable, str(absolute_script_path)]

    logger.line("")
    logger.line("=" * 80)
    logger.line(f"[{timestamp()}] Step {step_number}/{total_steps}: {name}")
    logger.line(f"Script: {script_path}")
    logger.line(f"Command: {' '.join(command)}")

    started = time.perf_counter()
    process = subprocess.Popen(
        command,
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )

    assert process.stdout is not None
    for line in process.stdout:
        logger.write(line)

    return_code = process.wait()
    duration = time.perf_counter() - started
    logger.line(f"[{timestamp()}] Finished: {name}")
    logger.line(f"Duration: {duration:.2f}s")
    logger.line(f"Exit code: {return_code}")
    return return_code


def main() -> int:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"live_pipeline_{run_id}.log"
    latest_log_path = LOG_DIR / "latest_run.log"

    logger = TeeLogger(log_path)
    exit_code = 0

    try:
        logger.line(f"Live pipeline run started: {timestamp()}")
        logger.line(f"Project root: {PROJECT_ROOT}")
        logger.line("Mode: operational 12h run")
        logger.line("LDA retraining: disabled")
        logger.line("Dashboard modification: disabled")
        logger.line("Raw dataset deletion: disabled")

        for index, (name, script_path) in enumerate(PIPELINE_STEPS, start=1):
            step_exit_code = run_step(index, len(PIPELINE_STEPS), name, script_path, logger)
            if step_exit_code != 0:
                logger.line("")
                logger.line(f"Pipeline stopped because step failed: {name}")
                exit_code = step_exit_code
                break

        if exit_code == 0:
            logger.line("")
            logger.line(f"Live pipeline completed successfully: {timestamp()}")
        else:
            logger.line("")
            logger.line(f"Live pipeline failed: {timestamp()}")
    finally:
        logger.close()
        shutil.copyfile(log_path, latest_log_path)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
