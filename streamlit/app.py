# 1. Import libraries
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# 2. Page configuration
st.set_page_config(
    page_title="HR Analytics Platform",
    layout="wide"
)


# 3. Title
st.title("HR Analytics Platform")

st.write(
    "AI-powered employee attrition prediction and workforce analytics"
)


# 4. Define project paths

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "xgboost_final_model.pkl"

DATA_PATH = BASE_DIR / "data" / "processed" / "hr_feature_engineered.csv"


# 5. Load trained model

model = joblib.load(MODEL_PATH)


# 6. Load processed HR data

df = pd.read_csv(DATA_PATH)


# 7. Prepare features

X = df.drop("Attrition", axis=1)


# ======================================
# Workforce Overview Dashboard
# ======================================

st.header("Workforce Overview")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Employees",
        len(df)
    )


with col2:
    attrition_rate = df["Attrition"].mean()

    st.metric(
        "Attrition Rate",
        f"{attrition_rate:.1%}"
    )


with col3:
    st.metric(
        "Number of Features",
        X.shape[1]
    )


# ======================================
# Employee Attrition Prediction
# ======================================

st.header("Employee Attrition Prediction")


employee_index = st.number_input(
    "Select Employee Index",
    min_value=0,
    max_value=len(X)-1,
    value=0
)


# Select employee

employee = X.iloc[[employee_index]]


# Predict probability

risk_probability = model.predict_proba(employee)[0][1]


st.metric(
    "Attrition Risk Probability",
    f"{risk_probability:.1%}"
)


# Risk classification
import shap
if risk_probability >= 0.5:
    st.error("High Risk of Attrition")
else:
    st.success("Low Risk of Attrition")
employee = X.iloc[[employee_index]]

# SHAP Explanation

st.header("Why did the model make this prediction?")


explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(employee)


feature_importance = pd.DataFrame({
    "Feature": employee.columns,
    "SHAP Value": shap_values[0]
})


feature_importance["Impact"] = feature_importance["SHAP Value"].abs()


feature_importance = feature_importance.sort_values(
    "Impact",
    ascending=False
)


st.dataframe(
    feature_importance.head(10)
)

