import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import io
# Set Streamlit Page Layout
st.set_page_config(page_title="Financial Analytics Dashboard", layout="wide")

# --- DATA EXTRACTION FUNCTIONS ---

@st.cache_data
def get_stock_data(ticker_symbol):
    """Fetch historical stock price data using yfinance."""
    try:
        ticker = yf.Ticker(ticker_symbol)
        df = ticker.history(period="max")
        df.reset_index(inplace=True)
        
        # Clean out any empty rows
        df.dropna(subset=['Close'], inplace=True)
        
        if df.empty:
            return pd.DataFrame()

        # Calculate metrics
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['SMA_200'] = df['Close'].rolling(window=200).mean()
        df['Daily_Return'] = df['Close'].pct_change()
        return df
    except Exception as e:
        st.error(f"Error fetching stock data for {ticker_symbol}: {e}")
        return pd.DataFrame()

@st.cache_data
def get_revenue_data(url):
    """Scrape revenue data using BeautifulSoup with error handling."""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table")
        
        # Locate the table containing quarterly revenue
        target_table = None
        for table in tables:
            if "Quarterly Revenue" in str(table):
                target_table = table
                break
                
        if target_table is None:
            return pd.DataFrame()

        # Wrap HTML string in io.StringIO to prevent file path error
        df = pd.read_html(io.StringIO(str(target_table)))[0]
        df.columns = ["Date", "Revenue"]
        
        # Data Cleaning
        df["Revenue"] = df["Revenue"].astype(str).str.replace(r"[\$,]", "", regex=True)
        df.dropna(subset=["Revenue"], inplace=True)
        df = df[df["Revenue"] != ""]
        df["Revenue"] = df["Revenue"].astype(float)
        df["Date"] = pd.to_datetime(df["Date"])
        
        return df
    except Exception as e:
        st.error(f"Error scraping revenue data: {e}")
        return pd.DataFrame()

# --- INTERACTIVE DASHBOARD UI ---

st.title("📈 Interactive Financial Performance Visualizer")
st.markdown("Analyze historical stock price movements against quarterly corporate revenues.")

# Sidebar Controls
st.sidebar.header("User Options")
selected_asset = st.sidebar.selectbox("Select Asset", ["Tesla (TSLA)", "GameStop (GME)"])

if selected_asset == "Tesla (TSLA)":
    ticker = "TSLA"
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
else:
    ticker = "GME"
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/gme_revenue.htm"

# Fetch Data
stock_df = get_stock_data(ticker)
revenue_df = get_revenue_data(url)

# Display Key Metrics
if not stock_df.empty:
    col1, col2, col3 = st.columns(3)
    
    # Safely extract latest price
    latest_price = stock_df['Close'].dropna().iloc[-1] if not stock_df['Close'].dropna().empty else None
    latest_price_str = f"${round(latest_price, 2)}" if latest_price is not None else "N/A"
    
    volatility = round(stock_df['Daily_Return'].std() * (252 ** 0.5) * 100, 2) if 'Daily_Return' in stock_df else "N/A"
    latest_rev = f"${revenue_df['Revenue'].iloc[0]:,.0f}M" if not revenue_df.empty else "N/A"
    
    col1.metric("Current Stock Price", latest_price_str)
    col2.metric("Annualized Volatility", f"{volatility}%")
    col3.metric("Latest Quarterly Revenue", latest_rev)
    # --- PLOTLY INTERACTIVE CHART ---
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Stock Price Trace
    fig.add_trace(
        go.Scatter(x=stock_df['Date'], y=stock_df['Close'], name="Stock Price ($)", line=dict(color="blue")),
        secondary_y=False
    )
    
    # 50-Day Moving Average
    fig.add_trace(
        go.Scatter(x=stock_df['Date'], y=stock_df['SMA_50'], name="50-Day SMA", line=dict(color="orange", dash="dash")),
        secondary_y=False
    )

    # Revenue Bar Trace
    if not revenue_df.empty:
        fig.add_trace(
            go.Bar(x=revenue_df['Date'], y=revenue_df['Revenue'], name="Quarterly Revenue ($)", opacity=0.4),
            secondary_y=True
        )

    fig.update_layout(
        title_text=f"{selected_asset}: Stock Price vs. Quarterly Revenue",
        xaxis_title="Date",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_yaxes(title_text="Stock Price ($)", secondary_y=False)
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=True)

    st.plotly_chart(fig, use_container_width=True)