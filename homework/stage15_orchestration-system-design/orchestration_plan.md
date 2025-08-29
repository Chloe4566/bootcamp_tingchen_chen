# Stage 15: Orchestration & System Design

## Pipeline Decomposition

My project can be framed as a 5-step pipeline:

1. **Ingestion**
   - Inputs: external API, raw CSV files
   - Outputs: `/data/raw/*.csv`
   - Idempotent: Yes (re-download overwrites with the same schema)
   - Logging: success/failure messages, record file counts
   - Checkpoint: existence of raw files

2. **Cleaning & Preprocessing**
   - Inputs: `/data/raw/*.csv`
   - Outputs: `/data/processed/cleaned.csv`
   - Idempotent: Yes (deterministic transforms)
   - Logging: number of rows dropped/filled, missing-value summary
   - Checkpoint: cleaned file created and row count logged

3. **Feature Engineering**
   - Inputs: `/data/processed/cleaned.csv`
   - Outputs: `/data/processed/features.csv`
   - Idempotent: Yes (feature code deterministic given same input)
   - Logging: distribution summaries, feature columns added
   - Checkpoint: features file saved with schema hash

4. **Model Training**
   - Inputs: `/data/processed/features.csv`
   - Outputs: `/model/model.pkl`, metrics.json
   - Idempotent: Partially (depends on random seed)
   - Logging: metrics (RMSE, R²), training duration
   - Checkpoint: model persisted, metrics file generated

5. **Reporting**
   - Inputs: `/model/model.pkl`, metrics.json
   - Outputs: `/reports/summary.md`, charts in `/reports/images/`
   - Idempotent: Yes
   - Logging: confirm reports generated, plot file names
   - Checkpoint: report artifacts exist

---

## Dependencies (DAG)


- Cleaning cannot start until ingestion succeeds.  
- Model training requires engineered features.  
- Reporting depends on trained model & metrics.  
- Ingestion and reporting are not parallelizable; feature engineering and training can be batched if multiple datasets.

---

## Reliability & Monitoring

- **Logging:** Simple `logging` module to record INFO and ERROR events in `/logs/`.  
- **Checkpoints:** File existence + row count + schema hash.  
- **Retry:** Ingestion retried 3 times with exponential backoff. Other stages fail-fast with error logs.  
- **Alert:** Email or Slack notification when model metrics drop below threshold.

---

## Automation Decisions

- **Automate Now:** Cleaning, feature engineering, training (can be wrapped in simple CLI Python scripts). These are repetitive and deterministic.  
- **Manual for Now:** Scenario design, stakeholder reporting, and dashboard polish remain manual because they require interpretation.  
- **Future Automation:** Full scheduling (cron/Prefect/Airflow) once pipeline stabilizes.
