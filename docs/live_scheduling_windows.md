# Live Pipeline Scheduling on Windows

This project uses an operational live pipeline that can run every 12 hours.
The scheduled run does not retrain LDA, does not modify dashboard files, and
does not delete the raw live dataset.

## Operational Pipeline

Run target:

```text
run_live_pipeline.bat
```

The batch file runs:

```text
scripts\run_live_pipeline.py
```

The orchestrator executes the live pipeline in this order:

1. `scripts/00_collect_live_sources.py`
2. `scripts/00b_inspect_live_dataset.py`
3. `scripts/01_prepare_live_social_news_dataset.py`
4. `scripts/02_live_filter_noise.py`
5. `scripts/03_live_preprocess_text.py`
6. `scripts/04_live_assign_topics_existing_live_lda.py`
7. `scripts/04c_apply_live_topic_labels.py`
8. `scripts/05_live_sentiment_vader.py`
9. `scripts/06_live_temporal_aggregation.py`
10. `scripts/07_live_compute_p2_index.py`

## Windows Task Scheduler

1. Open **Task Scheduler**.
2. Select **Create Task**.
3. Set a clear name, for example `Cyber Threat Live Pipeline`.
4. In **Triggers**, create two daily triggers:
   - daily at `00:00`;
   - daily at `12:00`.
5. In **Actions**, create one action:
   - Program/script: full path to `run_live_pipeline.bat`;
   - Start in: project root directory.
6. Save the task.
7. After a run, verify:

```text
logs\live_pipeline\latest_run.log
```

Timestamped logs are also saved as:

```text
logs\live_pipeline\live_pipeline_YYYYMMDD_HHMMSS.log
```

## LDA Retraining Policy

The scheduled operational run uses the existing official live LDA model in:

```text
models\live_lda_model\
```

It only assigns topics with the saved model. It must not call:

```text
scripts\04_live_train_lda_baseline.py
```

LDA retraining remains a manual or separately scheduled maintenance step.
