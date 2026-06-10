<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Order Priority Prediction App</title>

<style>
    body{
        font-family: Arial, sans-serif;
        line-height: 1.8;
        color: #333;
        max-width: 1200px;
        margin: auto;
        padding: 20px;
        background-color: #f8f9fa;
    }

    .container{
        background: #fff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    h1{
        text-align: center;
        color: #2c3e50;
    }

    h2{
        color: #34495e;
        border-bottom: 2px solid #ddd;
        padding-bottom: 5px;
        margin-top: 30px;
    }

    .feature-card{
        background: #f4f6f8;
        padding: 15px;
        margin: 10px 0;
        border-left: 5px solid #3498db;
        border-radius: 5px;
    }

    ul{
        padding-left: 20px;
    }

    code{
        background: #eee;
        padding: 2px 5px;
        border-radius: 4px;
    }

    .highlight{
        background: #eafaf1;
        padding: 10px;
        border-left: 5px solid #27ae60;
        border-radius: 5px;
    }

    .author{
        text-align: center;
        margin-top: 30px;
        font-size: 18px;
        font-weight: bold;
    }

    a{
        color: #0077cc;
        text-decoration: none;
    }

    a:hover{
        text-decoration: underline;
    }
</style>
</head>

<body>

<div class="container">

<h1>📦 Order Priority Prediction App</h1>

<h2>📖 Overview</h2>

<p>
This project is a <strong>Machine Learning-powered web application</strong> built using
<strong>Streamlit</strong> that predicts <strong>Order Priority</strong> from e-commerce order data.
The application allows users to upload a CSV file, generate predictions using both
<strong>Random Forest</strong> and <strong>CatBoost</strong> models, compare results, visualize insights
through interactive dashboards, and download prediction outputs.
</p>

<h2>✨ Features</h2>

<div class="feature-card">
    <h3>🌲 Random Forest Model</h3>
    <ul>
        <li>Predicts Order Priority from uploaded order data</li>
        <li>Displays prediction results</li>
        <li>Interactive dashboard with KPIs and visualizations</li>
        <li>Download predictions as CSV</li>
    </ul>
</div>

<div class="feature-card">
    <h3>🐈 CatBoost Model</h3>
    <ul>
        <li>Predicts Order Priority using CatBoost</li>
        <li>Displays prediction results</li>
        <li>Interactive dashboard with KPIs and visualizations</li>
        <li>Download predictions as CSV</li>
    </ul>
</div>

<h2>📊 Dashboard Analytics</h2>

<h3>Key Performance Indicators (KPIs)</h3>

<ul>
    <li>Total Orders</li>
    <li>Unique Priority Levels</li>
    <li>Most Common Priority</li>
    <li>Least Frequent Priority</li>
</ul>

<h3>Visualizations</h3>

<ul>
    <li>Count of Orders by Priority (Bar Chart)</li>
    <li>Priority Distribution (Pie Chart)</li>
    <li>Priority vs Category Heatmap</li>
    <li>Sales vs Priority (Horizontal Bar Chart)</li>
    <li>Priority Count Summary Table</li>
</ul>

<h2>🛠️ Technologies Used</h2>

<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>Scikit-learn</li>
    <li>Random Forest Classifier</li>
    <li>CatBoost</li>
</ul>

<h2>📂 Project Structure</h2>

<pre>
cat_cols.joblib
e-commerce
order_priority_feature_encoders.pkl
order_priority_model.cbm
order_priority_prediction_catboost
order_priority_prediction_random_forest
order_priority_target_encoder.pkl
orderpriority_randomforest.pkl
pred order priority
rf_catboost.py
rf_feature_columns.pkl
</pre>

<h2>🚀 Instructions for Running the Model</h2>

<ol>
    <li>
        Download <code>orderpriority_randomforest.pkl</code> from:
        <br>
        <a href="https://drive.google.com/drive/folders/1truJ6yMuA5KKVZldqTCEmxBHxmGmLSex?usp=drive_link">
            Google Drive
        </a>
    </li>

    <li>
        Download the remaining project files from:
        <br>
        <a href="https://github.com/jayant-kadam/order-priority-prediction">
            GitHub Repository
        </a>
    </li>

    <li>Create a project folder and place all downloaded files inside it.</li>

    <li>Run <code>rf_catboost.py</code> using your preferred IDE.</li>

    <li>
        Upload the <code>pred order priority</code> CSV file and the model will:
        <ul>
            <li>Predict Order Priority</li>
            <li>Generate a dashboard with analytics</li>
        </ul>
    </li>

    <li>Input data must be provided in CSV format.</li>

    <li>
        The input file must contain the following columns:
        <br><br>

        <div class="highlight">
        ROW ID, Order ID, Order Date, Ship Date, Ship Mode,
        Customer ID, Customer Name, Segment, City, State,
        Country, Market, Region, Product ID, Category,
        Sub-Category, Product Name, Sales, Quantity,
        Discount, Shipping Cost, Profit, Order Year,
        Order Month, Order Day, Ship Year, Ship Month,
        Ship Day, Delivery Time, Cost
        </div>
    </li>
</ol>

<h2>🤖 Machine Learning Models</h2>

<h3>🌲 Random Forest</h3>

<p>
A supervised ensemble learning algorithm that combines multiple decision trees
to improve prediction accuracy and reduce overfitting.
</p>

<h3>🐈 CatBoost</h3>

<p>
A gradient boosting algorithm that handles categorical features efficiently
and often provides strong performance on structured datasets.
</p>

<h2>🔮 Future Enhancements</h2>

<ul>
    <li>Feature Importance Visualization</li>
    <li>Model Performance Comparison</li>
    <li>Prediction Confidence Scores</li>
    <li>Cloud Deployment</li>
    <li>Additional Machine Learning Models</li>
    <li>Advanced Filtering and Reporting</li>
</ul>

<h2>👨‍💻 Author</h2>

<div class="author">
    Jayant Kadam <br>
    Aspiring Data Analyst
</div>

</div>

</body>
</html>
