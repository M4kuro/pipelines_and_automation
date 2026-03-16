# Automated ETL Pipeline for Video Game Sales Analytics 
![Status](https://img.shields.io/badge/status-actively_developing-blue)


## Overview
The goal was to design a scalable and configurable data pipeline that separates generic pipeline logic from dataset-specific business transformations and produces an analytics-ready fact table for BI tools.

---

## Project Goals
- Build a reusable ETL pipeline structure
- Separate core logic from dataset-specific transformations
- Enforce semantic data quality (not just technical cleaning)
- Produce a clean fact table for analytics and dashboards
- Keep the pipeline config-driven and easy to extend

---

## Tech Stack
- **Python**
- **Pandas**
- **YAML**
- **Power BI**
- Git / GitHub

---

## Dataset
The dataset used in this project comes from Kaggle:

**Video Game Sales Dataset**  
https://www.kaggle.com/datasets/gregorut/videogamesales

The raw CSV file is stored in the `data/raw` directory and processed through the ETL pipeline.


## Repository Structure
```
pipelines_and_automation/
│
├── core/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── pipelines/
│   └── videogame_sales/
│       ├── main.py
│       ├── transform_vgsales.py
│       └── config.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── archive/
├── reports/
│   └── videogame_sales/
├── requirements.txt
├── README.md
└── .gitignore
```


---

## Pipeline Flow
```
Raw CSV
↓
Extract (core)
↓
Standard Transform (core)
↓
Business Transform (videogame_sales)
↓
Analytics-ready Fact Table
↓
Power BI Dashboard
```

---

## Data Transformation Highlights
- Standardized column naming (lowercase, snake_case)
- Semantic validation of year values
- Reshaped wide regional sales data into long format
- Aggregated sales into a clean fact table


### Final Fact Table Schema

| Column       | Description                                   |
|--------------|-----------------------------------------------|
| year         | Release year                                  |
| genre        | Game genre                                    |
| region       | Sales region (NA, EU, JP, Other)              |
| total_sales  | Aggregated sales for the given year/region    |



Each row represents total video game sales for a given **genre**, **region**, and **year**.

---

## Configuration-Driven Execution
Pipeline behavior is controlled via `config.yaml`:

```
raw_path: data/raw/vgsales.csv
output_path: data/processed/vgsales_fact.csv
```

## How to Run
From the project root:

```bash
python -m pipelines.videogame_sales.main
```

## Output
- Clean, analytics-ready CSV stored in data/processed
- Power BI dashboard built on top of the fact table

## Key Takeaways
- Designed a reusable ETL framework instead of a one-off script
- Applied proper separation of concerns
- Focused on semantic correctness for analytics
- Built a pipeline ready for automation and scheduling

## Next Improvements
- Add scheduling (Task Scheduler / cron)
- Add API-based data ingestion
- Extend pipeline to additional datasets
  

