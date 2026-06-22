import streamlit as st
#to create a web app.

import pandas as pd
#to read and work with CSV/Excel data.

import numpy as np
#Helps with numerical operations (arrays, math).

import joblib
#to load saved ML models.

import matplotlib.pyplot as plt
#to create graphs.

import seaborn as sns
#to create graphs.

from catboost import CatBoostClassifier
#to loads and runs the CatBoost ML model.

# -------------------------------------------------------
# PAGE SETUP
# -------------------------------------------------------
st.set_page_config(page_title="Order Priority Prediction App", layout="wide")
#Sets the app title seen on the browser tab.
st.title("📦 Order Priority Prediction App")
st.write("Upload a CSV file to predict order priority using Random Forest and CatBoost models.")

# -------------------------------------------------------
# LOAD MODELS AND ENCODERS
# -------------------------------------------------------
rf_model = joblib.load("model/orderpriority_randomforest.pkl")
rf_target_encoder = joblib.load("model/order_priority_target_encoder.pkl")
rf_feature_encoders = joblib.load("model/order_priority_feature_encoders.pkl")
rf_features = joblib.load("model/rf_feature_columns.pkl")

catboost_model = CatBoostClassifier()
catboost_model.load_model("model/order_priority_model.cbm")
catboost_cat_cols = joblib.load("model/cat_cols.joblib")

# -------------------------------------------------------
# FILE UPLOADER
# -------------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📘 Uploaded Data Preview")
    st.dataframe(df.head())

    tab1, tab2 = st.tabs(["🌲 Random Forest Model", "🐈 CatBoost Model"])

    # =====================================================
    # 🔶 TAB 1 — RANDOM FOREST MODEL
    # =====================================================
    with tab1:
        st.subheader("🌲 Random Forest — Order Priority Prediction Preview")

        df_rf = df.copy()
	#Making a separate copy so original data is safe.

        missing_cols = [col for col in rf_features if col not in df_rf.columns]
        if missing_cols:
            st.error(f"❌ Missing required columns for Random Forest: {missing_cols}")
	#Checking if uploaded CSV is missing any columns the model needs.

        else:
            df_rf_model = df_rf[rf_features].copy()

            for col, le in rf_feature_encoders.items():
                df_rf_model[col] = le.transform(df_rf_model[col])

            rf_pred = rf_model.predict(df_rf_model)
            rf_pred_label = rf_target_encoder.inverse_transform(rf_pred)

            df_rf["Predicted Priority"] = rf_pred_label

            st.write("### 🔮 Predictions")
            st.dataframe(df_rf[["Order ID", "Predicted Priority"]].head())

        st.write("### 📊 Count of Each Predicted Priority (Random Forest)")

        st.dataframe(df_rf["Predicted Priority"].value_counts().reset_index().rename(
        columns={"Predicted Priority": "Type of Priority", "count": "Number of Counts"}))


        # -----------------------------
        # RF DASHBOARD
        # -----------------------------
        st.subheader("📊 Random Forest Dashboard")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Orders", len(df_rf))
        col2.metric("Unique Priorities", df_rf["Predicted Priority"].nunique())
        col3.metric("Most Common Priority", df_rf["Predicted Priority"].mode()[0])
        col4.metric("Least Frequent Priority", df_rf["Predicted Priority"].value_counts().idxmin())

        colA, colB = st.columns(2)

        with colA:
            st.write("### 📈 Count of Orders by Priority")
            fig, ax = plt.subplots()
            df_rf["Predicted Priority"].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        with colB:
            st.write("### 🥧 Priority Share")
            fig, ax = plt.subplots()
            df_rf["Predicted Priority"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
            st.pyplot(fig)

        colC, colD = st.columns(2)

        with colC:
            if "Category" in df.columns:
                st.write("### 🔥 Heatmap: Priority vs Category")
                pt = pd.crosstab(df_rf["Predicted Priority"], df["Category"])
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.heatmap(pt, annot=True, cmap="Greens", ax=ax)
                st.pyplot(fig)

        with colD:
            if "Sales" in df.columns:
                st.write("### 💰 Sales by Priority")
                fig, ax = plt.subplots()
                df_rf.groupby("Predicted Priority")["Sales"].sum().sort_values().plot(kind="barh", ax=ax)
                st.pyplot(fig)

        # # -----------------------------
        # # ⭐ FEATURE IMPORTANCE – RANDOM FOREST
        # # -----------------------------
        # st.write("### 📌 Feature Importance (Random Forest)")

        # importances = rf_model.feature_importances_
        # feature_names = rf_features

        # fi_rf = pd.DataFrame({
        #  "Feature": feature_names,
        #  "Importance": importances
        # }).sort_values(by="Importance", ascending=False)

        # fig, ax = plt.subplots(figsize=(8, 5))
        # sns.barplot(x="Importance", y="Feature", data=fi_rf, ax=ax)
        # plt.title("Random Forest Feature Importance")
        # st.pyplot(fig)







        # -----------------------------
        # ⭐ RF DOWNLOAD BUTTON
        # -----------------------------
        st.write("### 📥 Download Random Forest Output")

        rf_csv = df_rf.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Random Forest Predictions (CSV)",
            data=rf_csv,
            file_name="random_forest_predictions.csv",
            mime="text/csv"
        )

    # =====================================================
    # 🔶 TAB 2 — CATBOOST MODEL
    # =====================================================
    with tab2:
        st.subheader("🐈 CatBoost — Order Priority Prediction Preview")

        df_cb = df.copy()

        # Convert categorical columns
        for c in catboost_cat_cols:
            df_cb[c] = df_cb[c].astype(str)

        cb_pred = catboost_model.predict(df_cb)
        df_cb["Predicted Priority"] = cb_pred.ravel()

        st.write("### 🔮 Predictions")
        st.dataframe(df_cb[["Order ID", "Predicted Priority"]].head())

        st.write("### 📊 Count of Each Predicted Priority (CatBoost)")
        st.dataframe(df_cb["Predicted Priority"].value_counts().reset_index().rename(
        columns={"Predicted Priority": "Type of Priority", "count": "Number of Counts"}))


        # -----------------------------
        # CATBOOST DASHBOARD
        # -----------------------------
        st.subheader("📊 CatBoost Dashboard")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Orders", len(df_cb))
        col2.metric("Unique Priorities", df_cb["Predicted Priority"].nunique())
        col3.metric("Most Common Priority", df_cb["Predicted Priority"].mode()[0])
        col4.metric("Least Frequent Priority", df_cb["Predicted Priority"].value_counts().idxmin())

        colA, colB = st.columns(2)

        with colA:
            st.write("### 📈 Count of Orders by Priority")
            fig, ax = plt.subplots()
            df_cb["Predicted Priority"].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        with colB:
            st.write("### 🥧 Priority Share")
            fig, ax = plt.subplots()
            df_cb["Predicted Priority"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
            st.pyplot(fig)

        colC, colD = st.columns(2)

        with colC:
            if "Category" in df.columns:
                st.write("### 🔥 Heatmap: Priority vs Category")
                pt = pd.crosstab(df_cb["Predicted Priority"], df["Category"])
                fig, ax = plt.subplots(figsize=(8, 5))
                sns.heatmap(pt, annot=True, cmap="Greens", ax=ax)
                st.pyplot(fig)

        with colD:
            if "Sales" in df.columns:
                st.write("### 💰 Sales by Priority")
                fig, ax = plt.subplots()
                df_cb.groupby("Predicted Priority")["Sales"].sum().sort_values().plot(kind="barh", ax=ax)
                st.pyplot(fig)



        # # -----------------------------
        # # ⭐ FEATURE IMPORTANCE – CATBOOST
        # # -----------------------------
        # st.write("### 📌 Feature Importance (CatBoost)")

        # cb_importance = catboost_model.get_feature_importance()
        # cb_features = df_cb.drop(columns=["Predicted Priority"]).columns

        # fi_cb = pd.DataFrame({
        #  "Feature": cb_features,
        #  "Importance": cb_importance
        # }).sort_values(by="Importance", ascending=False)

        # fig, ax = plt.subplots(figsize=(8, 5))
        # sns.barplot(x="Importance", y="Feature", data=fi_cb, ax=ax)
        # plt.title("CatBoost Feature Importance")
        # st.pyplot(fig)




        # -----------------------------
        # ⭐ CATBOOST DOWNLOAD BUTTON
        # -----------------------------
        st.write("### 📥 Download CatBoost Output")

        cb_csv = df_cb.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download CatBoost Predictions (CSV)",
            data=cb_csv,
            file_name="catboost_predictions.csv",
            mime="text/csv"
        )
