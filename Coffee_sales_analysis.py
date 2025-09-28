# 📦 Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import streamlit as st

# 📥 Load Data
df = pd.read_csv("coffee_sales.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df.dropna(subset=['date', 'money'], inplace=True)

# 🧹 Feature Engineering
df['hour'] = df['datetime'].dt.hour
df['day'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month_name()

# 🎛️ Sidebar Filters
st.sidebar.header("🔍 Filter Data")
start_date = st.sidebar.date_input("Start Date", df['date'].min())
end_date = st.sidebar.date_input("End Date", df['date'].max())
coffee_options = st.sidebar.multiselect("Coffee Type", df['coffee_name'].unique(), default=df['coffee_name'].unique())
payment_options = st.sidebar.multiselect("Payment Method", df['cash_type'].unique(), default=df['cash_type'].unique())

# 🧼 Apply Filters
filtered_df = df[
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date)) &
    (df['coffee_name'].isin(coffee_options)) &
    (df['cash_type'].isin(payment_options))
]

# 📁 Download filtered data
st.sidebar.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_coffee_sales.csv',
    mime='text/csv'
)

# 📊 Plot Functions
def plot_sales_by_coffee(data):
    coffee_sales = data.groupby('coffee_name')['money'].sum().sort_values()
    plt.figure(figsize=(8, 5))
    coffee_sales.plot(kind='barh', color='sienna')
    plt.title("Total Sales by Coffee Type")
    plt.xlabel("Revenue")
    st.pyplot(plt)

def plot_hourly_sales(data):
    hourly_sales = data.groupby('hour')['money'].sum()
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=hourly_sales.index, y=hourly_sales.values, marker='o')
    plt.title("Hourly Sales Trend")
    plt.xlabel("Hour of Day")
    plt.ylabel("Revenue")
    st.pyplot(plt)

def plot_payment_method(data):
    payment_counts = data['cash_type'].value_counts()
    plt.figure(figsize=(5, 5))
    payment_counts.plot.pie(autopct='%1.1f%%', colors=['gold', 'lightblue'])
    plt.title("Payment Method Distribution")
    st.pyplot(plt)

def forecast_sales(data):
    daily_sales = data.groupby('date')['money'].sum().reset_index()
    daily_sales.columns = ['ds', 'y']
    model = Prophet()
    model.fit(daily_sales)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    fig1 = model.plot(forecast)
    st.pyplot(fig1)

    fig2 = model.plot_components(forecast)
    st.pyplot(fig2)

    # 📁 Download forecast data
    forecast_csv = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(index=False).encode('utf-8')
    st.download_button("Download Forecast Data", data=forecast_csv, file_name="forecast.csv", mime="text/csv")

# 🧠 Dashboard Layout
st.title("☕ Coffee Sales Analysis Dashboard")
st.write(f"Showing data from **{start_date}** to **{end_date}** for selected coffee types and payment methods.")

st.subheader("📊 Sales by Coffee Type")
plot_sales_by_coffee(filtered_df)

st.subheader("🕒 Hourly Sales Trend")
plot_hourly_sales(filtered_df)

st.subheader("💳 Payment Method Distribution")
plot_payment_method(filtered_df)

st.subheader("📈 Forecasted Sales")
forecast_sales(filtered_df)

# 🔗 Optional Tableau Embed (if available)
# tableau_url = "https://public.tableau.com/views/YourDashboardName"
# st.markdown(f'<iframe src="{tableau_url}" width="1000" height="600"></iframe>', unsafe_allow_html=True)
