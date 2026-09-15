# HR Analytics & Predictive Attrition Platform

## Overview

HR Analytics & Predictive Attrition Platform is an end-to-end machine learning project designed to analyze workforce data and predict employee attrition risk.

The project combines data preprocessing, feature engineering, machine learning, explainable AI, and interactive dashboards to support data-driven HR decision making.

The platform demonstrates a complete machine learning lifecycle:

- Data preparation and validation
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Hyperparameter optimization
- Explainable AI using SHAP
- Interactive prediction application using Streamlit

The goal is to help HR teams identify employee attrition patterns, understand key risk factors, and support proactive workforce decisions.

---

# Features

- HR data preprocessing and validation
- Exploratory Data Analysis (EDA)
- Feature engineering pipeline
- Employee attrition prediction
- XGBoost classification model
- Hyperparameter tuning
- Model evaluation
- SHAP explainability
- Workforce analytics dashboard
- Interactive Streamlit web application
- Employee-level attrition risk prediction

---

# Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Power BI
- Git/GitHub

---

# Dataset

This project uses the publicly available **IBM HR Analytics Employee Attrition Dataset**.

The dataset contains employee demographic, job-related, and satisfaction information used to analyze workforce patterns and predict employee attrition risk.

---

# Project Workflow

```text
IBM HR Analytics Dataset
          |
          ▼
Data Validation & Preprocessing
          |
          ▼
Exploratory Data Analysis (EDA)
          |
          ▼
Feature Engineering
          |
          ▼
XGBoost Model Training
          |
          ▼
Hyperparameter Optimization
          |
          ▼
Model Evaluation
          |
          ▼
SHAP Explainability
          |
          ▼
Streamlit HR Analytics Application
```

---

# Project Structure

```text
hr-analytics-platform/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_SHAP.ipynb
│
├── src/
│   ├── etl.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── predict.py
│   └── explain.py
│
├── models/
│   ├── xgboost_final_model.pkl
│   └── xgboost_model.pkl
│
├── streamlit/
│   └── app.py
│
├── images/
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# Machine Learning Model

The project uses an **XGBoost classification model** to predict employee attrition.

The workflow includes:

- Feature preparation
- Model training
- Hyperparameter optimization
- Performance evaluation
- Feature importance analysis

The final trained model is saved and integrated into the Streamlit application for prediction.

---

# Explainable AI with SHAP

SHAP (SHapley Additive exPlanations) is used to interpret model predictions.

The explainability component identifies the main factors influencing individual employee predictions.

Example factors:

- OverTime
- JobRole
- DistanceFromHome
- MonthlyIncome
- StockOptionLevel
- DailyRate

This helps transform machine learning predictions into understandable HR insights.

---

# Streamlit Application

The interactive Streamlit application provides:

- Workforce overview metrics
- Employee attrition risk prediction
- Probability-based risk scoring
- High/low risk classification
- SHAP-based explanation of predictions

Example:

```text
Employee Attrition Prediction

Attrition Risk Probability: 97.6%

Risk Level:
High Risk of Attrition
```

The application allows users to understand not only **what the model predicts**, but also **why the model made that prediction**.

---

# How to Run

## Install dependencies

```bash
pip install -r requirements.txt
```

## Launch Streamlit application

```bash
py -m streamlit run streamlit/app.py
```

The application will open locally in your browser.

---

# Future Improvements

- FastAPI model deployment
- Docker containerization
- Cloud deployment
- Model monitoring
- Automated retraining pipeline
- CI/CD integration
- Enhanced workforce analytics dashboards

---

# License

This project is intended for educational and portfolio purposes.
