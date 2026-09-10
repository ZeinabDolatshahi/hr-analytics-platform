# HR Analytics & Predictive Attrition Platform

## Overview

HR Analytics & Predictive Attrition Platform is an end-to-end machine learning project designed to analyze workforce data and predict employee attrition.

The project combines data engineering, business intelligence, and machine learning to support data-driven HR decision making. It demonstrates a complete analytics workflow, from data preprocessing and feature engineering to predictive modeling, explainable AI, and interactive dashboards.

The goal is to build a reusable analytics platform that enables HR professionals to explore employee data, identify attrition risk factors, and generate actionable insights through visual dashboards and predictive models.

---

## Features

- HR data preprocessing
- Data validation
- Feature engineering
- Employee attrition prediction
- XGBoost machine learning model
- SHAP explainability
- Power BI dashboard
- Streamlit web application
- Interactive employee risk prediction

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Power BI
- Streamlit
- Git

---

## Dataset

This project uses the publicly available **IBM HR Analytics Employee Attrition Dataset**, a widely used benchmark dataset for employee attrition prediction and HR analytics research.

---

## Project Roadmap

- [x] Project design
- [x] ETL pipeline
- [x] Exploratory data analysis (EDA)
- [ ] Feature engineering
- [x] Train XGBoost model
- [x] Model evaluation
- [ ] SHAP explainability
- [ ] Power BI dashboard
- [ ] Streamlit application
- [ ] FastAPI integration
- [ ] Documentation

---

## Project Structure

```text
hr-analytics-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_XGBoost_Model.ipynb
│   ├── 04_Model_Evaluation.ipynb
│   └── 05_SHAP_Explainability.ipynb
│
├── src/
│   ├── etl.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│   ├── xgboost_model.pkl
│   └── label_encoder.pkl
│
├── powerbi/
│   ├── dashboard.pbix
│   └── dashboard_preview.png
│
├── streamlit/
│   └── app.py
│
├── images/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Workflow

```text
IBM HR Analytics Dataset
          │
          ▼
ETL Pipeline
(Load → Validate → Clean)
          │
          ▼
Exploratory Data Analysis (EDA)
          │
          ▼
Feature Engineering
          │
          ▼
Train XGBoost Model
          │
          ▼
Model Evaluation
          │
          ▼
SHAP Explainability
      ┌───┴───┐
      ▼       ▼
 Power BI  Streamlit
 Dashboard  Web App
          │
          ▼
      FastAPI (Optional)

---

## Future Improvements

- FastAPI deployment
- Docker support
- Cloud deployment
- Model monitoring
- Automated retraining pipeline

---

## License

This project is intended for educational and portfolio purposes.
