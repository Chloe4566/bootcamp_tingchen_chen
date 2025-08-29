# Lifecycle Framework Guide — Final Project

## Project Overview
- **Title:** 
- **Objective (1–2 lines):** 
- **Primary Stakeholders:** 
- **Key Dataset(s):** 

---

## Lifecycle Mapping (Stage → What you did → Evidence)
| Lifecycle Stage | What I did (summary) | Where (path / file) | Evidence (note/metric) |
|---|---|---|---|
| Problem framing | Business question, success metric | README.md | Success metric defined |
| Data acquisition | API/scrape/load raw | homework/stage04_data-acquisition/... | Raw CSVs saved |
| Storage & layout | raw vs processed, env paths | homework/stage05_data-storage/... | IO utils & folders |
| Preprocessing | cleaning functions & docs | homework/stage06_data-preprocessing/... | Cleaned file saved |
| EDA | profiling + plots + insights | homework/stage08_eda/... | 3+ plots, notes |
| Feature engineering | 2–3 features + rationale | homework/stage09_feature-engineering/... | Engineered CSV |
| Modeling (regression) | train/test, metrics, residuals | homework/stage10a_modeling/... | R²/RMSE + diagnostics |
| Time / classification | lags/rolling + pipeline | homework/stage10b_modeling... | MAE/F1 + plots |
| Evaluation & risk | bootstrap CI, scenarios, subgroups | homework/stage11_evaluation-risk/... | CI/side-by-side charts |
| Stakeholder deliverable | summary + visuals + sensitivity | homework/stage12_final-deliverable/... | images + report |
| Productization | src/, model.pkl, API | homework/stage13_productization/... | app.py + model.pkl |
| Deployment & monitoring | risks + metrics + owners | homework/stage14_deployment-monitoring/... | reflection.md |
| Orchestration | pipeline plan/DAG | homework/stage15_orchestration-system-design/... | orchestration_plan.md |
| Lifecycle review | this guide + repo polish | homework/stage16_lifecycle-review/... | ✅ |

---

## Repo Readiness Checklist
- [ ] **Clean tree:** `/data/`, `/src/`, `/notebooks/`, `/model/`, `/reports/`, `/deliverables/`
- [ ] **README at repo root** with: overview, quickstart, env/requirements, **lifecycle mapping section**
- [ ] **Stakeholder summary** (PDF/MD/slides) in `/deliverables/`
- [ ] **Requirements** files present (`requirements.txt` or `environment.yml`)
- [ ] **Reproducibility:** seeds set; notebooks run top-to-bottom; file paths relative
- [ ] **Model artifact:** `/model/model.pkl` (or equivalent) + reload demo
- [ ] **API/Dashboard (if present):** run instructions + minimal test
- [ ] **.gitignore** excludes `.env`, large raw, caches
- [ ] **No secrets** committed

---

## Stakeholder Summary (1–3 bullets)
- 
- 
- 

---

## Monitoring & Handoffs (short)
- **Data metrics:** freshness, null rate, schema hash (thresholds)
- **Model metrics:** rolling RMSE/R² (window & alert)
- **System metrics:** p95 latency, job success %
- **Business KPI:** approval/uptake rate
- **Owners & cadence:** who reviews which dashboard, retrain triggers

---

## Next Steps
- Near-term improvements:
- Longer-term roadmap:
