# Coffee-sales-Analysis
An interactive Streamlit dashboard to visualize, analyze, and forecast coffee shop sales.
Description:
An interactive Streamlit dashboard to visualize, analyze, and forecast coffee shop sales. This project helps coffee shop owners or analysts understand revenue patterns, peak hours, popular coffee types, and payment trends. Using Prophet, it provides a 30-day sales forecast with trend and seasonality insights, helping in inventory and sales planning.

Key Features:

Filter sales data by date, coffee type, and payment method.

Visualize total sales by coffee type (bar chart).

Track hourly sales trends (line chart).

Analyze payment method distribution (pie chart).

Forecast future daily sales with Prophet (including trend and seasonal components).

Download filtered data and forecast results as CSV.

Tech Stack:
Python, Streamlit, Pandas, Matplotlib, Seaborn, Prophet
☕ Coffee Sales Analysis Dashboard

An interactive Streamlit dashboard to analyze and forecast coffee shop sales.
This project helps visualize sales patterns, customer behavior, and future revenue trends using Prophet forecasting.

📌 Features

📥 Data Upload & Cleaning

Reads sales data (coffee_sales.csv)

Cleans invalid/missing values

Extracts useful time-based features (hour, day, month)

🎛️ Interactive Filters

Date range selection

Filter by coffee type

Filter by payment method

📊 Visualizations

Sales by Coffee Type → Bar chart of total revenue per coffee

Hourly Sales Trend → Line chart showing peak sales hours

Payment Method Distribution → Pie chart of payment methods used

📈 Forecasting with Prophet

30-day future sales prediction

Forecast components (trend, seasonality, holidays if applicable)

Option to download forecast results as CSV

📁 Export Options

Download filtered dataset

Download forecasted data

🛠️ Tech Stack

Python

Pandas → Data manipulation

Seaborn & Matplotlib → Data visualization

Streamlit → Interactive dashboard

Facebook Prophet → Time series forecasting

📂 Project Structure
📦 coffee-sales-dashboard
 ┣ 📜 app.py                # Main Streamlit app
 ┣ 📜 coffee_sales.csv      # Sample dataset
 ┣ 📜 requirements.txt      # Dependencies
 ┗ 📜 README.md             # Documentation

▶️ Run Locally

Clone this repository

git clone https://github.com/yourusername/coffee-sales-dashboard.git
cd coffee-sales-dashboard


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py


Open in your browser at http://localhost:8501/

📊 Example Dashboard

Sales by Coffee Type

Hourly Sales Trend

Payment Method Distribution

30-day Sales Forecast

📈 Forecasting Example

The app uses Prophet to forecast future daily sales.
You’ll see:

Forecast curve (predicted sales)

Uncertainty intervals (yhat_lower, yhat_upper)

Trend & seasonality decomposition

📥 Downloadable Reports

Filtered dataset → filtered_coffee_sales.csv

Forecast results → forecast.csv

🔮 Future Improvements

Add customer segmentation analysis

Include seasonal promotions/holiday effects

Integrate Tableau or Power BI dashboards

✨ Built with love for coffee and data.
