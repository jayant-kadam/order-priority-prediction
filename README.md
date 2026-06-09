📦 Order Priority Prediction App
Overview

This project is a Machine Learning-powered web application built using Streamlit that predicts Order Priority from e-commerce order data. The application allows users to upload a CSV file, generate predictions using both Random Forest and CatBoost models, compare results, visualize insights through interactive dashboards, and download prediction outputs.

Features
🌲 Random Forest Model
Predicts Order Priority from uploaded order data
Displays prediction results
Interactive dashboard with KPIs and visualizations
Download predictions as CSV
🐈 CatBoost Model
Predicts Order Priority using CatBoost
Displays prediction results
Interactive dashboard with KPIs and visualizations
Download predictions as CSV
📊 Dashboard Analytics

The application provides:

Key Performance Indicators (KPIs)
Total Orders
Unique Priority Levels
Most Common Priority
Least Frequent Priority
Visualizations
Count of Orders by Priority (Bar Chart)
Priority Distribution (Pie Chart)
Priority vs Category Heatmap
Sales vs Priority (Horizontal Bar Chart)
Priority Count Summary Table
Technologies Used
Python
Streamlit
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Random Forest Classifier
CatBoost
Project Structure
├── app.py
├── orderpriority_randomforest.pkl
├── order_priority_target_encoder.pkl
├── order_priority_feature_encoders.pkl
├── rf_feature_columns.pkl
├── order_priority_model.cbm
├── cat_cols.joblib
├── requirements.txt
└── README.md
