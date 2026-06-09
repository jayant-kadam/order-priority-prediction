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

Project Structure contains:
- cat_cols.joblib
- e-commerce
- order_priority_feature_encoders.pkl
- order_priority_model.cbm
- order_priority_prediction_catboost
- order_priority_prediction_random_forest
- order_priority_target_encoder.pkl
- orderpriority_randomforest.pkl (Download from Google Drive link mentioned below)
- pred order priority
- rf_catboost
- rf_feature_columns.pkl

Instructions for running the model.
1. Download orderpriority_randomforest.pkl from below link.
   https://drive.google.com/drive/folders/1truJ6yMuA5KKVZldqTCEmxBHxmGmLSex?usp=drive_link
2. Download rest of the files from github repository
   https://github.com/jayant-kadam/order-priority-prediction
3. Create a project folder.Copy and paste all downloaded file in project folder.
4. Run rf_catboost.py file using your preffered IDE.
5. Upload pred order priority file & model will predict order priority and  create dashboard.
6. To check order priority, input must be provided in .csv file.
7. Input file must contain following features / cploumns:
   ROW ID,	Order ID,	Order Date,	Ship Date, Ship Mode,	Customer ID,	Customer Name,	Segment,	City,	State,	Country,	Market,	Region,	Product ID,	Category,	Sub-Category,	Product Name,	Sales,	Quantity,	Discount,	Shipping Cost,	Profit,	Order Year,	Order Month,	Order Day,	Ship Year,	Ship Month,	Ship Day,	Delivery Time,	Cost.

Machine Learning Models <br>
Random Forest<br>
A supervised ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

CatBoost<br>
A gradient boosting algorithm that handles categorical features efficiently and often provides strong performance on structured datasets.

Future Enhancements
Feature Importance Visualization
Model Performance Comparison
Prediction Confidence Scores
Cloud Deployment
Additional Machine Learning Models
Advanced Filtering and Reporting

Author<br>
Jayant Kadam<br>
Aspiring Data Analyst

