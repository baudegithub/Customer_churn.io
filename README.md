# Customer Churn Prediction

This project follows a typical machine learning workflow for a churn prediction problem at PowerCo.

## Business objective

Identify customers at risk of churn and highlight the variables most associated with customer attrition, so that retention efforts can be prioritized more effectively.

## Typical ML project structure

```text
Customer_churn.io/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   ├── evaluation.py
│   └── train_pipeline.py
├── data/
│   ├── client_data.csv
│   └── price_data.csv
├── reports/
│   └── churn_summary.md
└── models/
    └── .gitkeep
```

## Notebook mapping

- 01_eda.ipynb: data understanding, descriptive analysis, and churn visualizations
- 02_feature_engineering.ipynb: feature creation, missing values, and pre-processing logic
- 03_modeling.ipynb: train/test split, model training, validation, and interpretation

## Project workflow

1. Load client and price datasets
2. Explore data quality and churn patterns
3. Engineer business-relevant features
4. Train and compare model candidates
5. Evaluate performance with business-focused metrics
6. Interpret results and provide recommendations

## How to run

```bash
pip install -r requirements.txt
python src/train_pipeline.py
```

## Data responsibilities

- `data_loader.py`: file loading and dataframe preparation
- `eda.py`: exploratory plots and business insights
- `feature_engineering.py`: transform raw fields into model-ready features
- `modeling.py`: model training, tuning, and prediction logic
- `evaluation.py`: metrics, confusion matrix, and reporting
- `train_pipeline.py`: orchestrates the full workflow

## Example output

The project is designed to produce:

- churn rate distributions
- customer segment insights
- engineered predictive features
- model scorecards and business recommendations

## Relevance to the original notebook

The notebook work is organized into the same standard ML steps used in production-ready pipelines:

- data preparation
- exploratory analysis
- feature engineering
- model training
- evaluation
- communication of findings

This structure makes the project easier to extend, test, and present to recruiters or stakeholders.

---

## Original project notes

This repository contains the customer churn project I worked on during the data scientist job simulation at BCG.

It explores customer churn in the PowerCo dataset using Python, Jupyter Notebook, and standard machine learning workflows.
