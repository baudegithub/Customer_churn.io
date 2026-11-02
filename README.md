# Customer Churn Prediction

This project follows a typical machine learning workflow for a churn prediction problem at PowerCo.

## Business objective

Identify customers at risk of churn and highlight the variables most associated with customer attrition so that retention efforts can be prioritized more effectively.

## Typical ML project structure

```text
Customer_churn.io/
├── README.md
├── requirements.txt
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_eda.py
│   ├── 03_feature_engineering.py
│   ├── 04_modeling.py
│   ├── 05_evaluation.py
│   └── 06_train_pipeline.py
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
├── models/
│   └── .gitkeep
└── notebooks/
    └── optional_notebooks_for_exploration
```

## Script mapping

- `01_load_data.py`: loads and validates the raw datasets
- `02_eda.py`: explores churn patterns and creates the visualizations
- `03_feature_engineering.py`: builds preparation features and transform logic
- `04_modeling.py`: trains candidate models and saves outputs
- `05_evaluation.py`: evaluates model performance and business impact
- `06_train_pipeline.py`: orchestrates the full workflow end-to-end

## Workflow

1. Load client and price data
2. Explore the data and detect churn patterns
3. Create business-oriented features
4. Train and compare models
5. Evaluate with relevant classification metrics
6. Communicate findings and recommendations

## How to run

```bash
pip install -r requirements.txt
python scripts/06_train_pipeline.py
```

## Data responsibilities

- `src/data_loader.py`: data input and format handling
- `src/eda.py`: exploratory charts and insight generation
- `src/feature_engineering.py`: feature creation and preprocessing logic
- `src/modeling.py`: model training logic
- `src/evaluation.py`: metrics and result analysis
- `src/train_pipeline.py`: end-to-end project runner

## Example output

The project is designed to produce:

- churn rate distributions
- customer segment insights
- engineered predictive variables
- model scorecards
- retention recommendations

## Project value

This project demonstrates a standard data science workflow:

- data preparation
- exploratory analysis
- feature engineering
- model training
- evaluation
- business communication

It is structured in a way that is easy to extend, understand, and present to recruiters or stakeholders.

---

This repository contains the customer churn project I worked on during the data scientist job simulation at BCG.
It focuses on understanding churn risk and prioritizing customer retention strategies for PowerCo.
