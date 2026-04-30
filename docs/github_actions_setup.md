# GitHub Actions Setup for the Live Pipeline

The live pipeline can run in GitHub Actions at 00:00 and 12:00 UTC without
keeping the local PC powered on.

## Setup Steps

1. Create a GitHub repository for this project.
2. Push the project to GitHub.
3. Verify that the official live LDA model is included:

```text
models/live_lda_model/
```

Required model files include:

```text
models/live_lda_model/lda_model.gensim
models/live_lda_model/dictionary.gensim
```

4. Verify that the workflow exists:

```text
.github/workflows/live_pipeline.yml
```

5. Open the repository on GitHub.
6. Open the **Actions** tab.
7. Select **Live Cyber Threat Pipeline**.
8. Run the workflow manually with **Run workflow**.
9. Check the workflow log for each pipeline step.
10. Check that the workflow creates an automatic commit when outputs change.

Expected commit message:

```text
chore: update live pipeline outputs [skip ci]
```

## Output Checks

After a successful run, verify the updated outputs:

```text
data/live/raw/live_items_raw.csv
data/live/processed/
reports/live/
dashboard/src/data/
```

If no output changes are produced, the workflow prints:

```text
No changes to commit
```

## Operational Policy

- The scheduled workflow runs at 00:00 and 12:00 UTC.
- The workflow can also be launched manually with `workflow_dispatch`.
- The workflow uses public social/news sources only: Reddit RSS, news/blog RSS, and GDELT DOC API.
- The workflow does not use CVE/NVD as an input source for P2.
- The workflow does not retrain LDA.
- The workflow uses the existing official live LDA model only for topic assignment.
- Dashboard UI changes remain manual and outside this scheduled run.
