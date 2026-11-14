# Financial Performance Visualizer & Analytics Dashboard

**Connecting corporate financial performance with stock market movements
through Python, data analysis, and interactive visualization.**

An end-to-end financial analytics project that combines quarterly
company revenue data with historical stock market prices. The
application uses Python to collect, process, and analyze financial data,
then presents the results through an interactive dashboard built with
Streamlit and Plotly.

The project explores how company-reported financial performance relates
to stock price behavior over time, bringing multiple financial data
sources together in one place.

------------------------------------------------------------------------

## Project Overview

Understanding a company's financial performance requires looking beyond
stock prices alone. Quarterly revenue provides insight into business
performance, while historical market data helps reveal how a stock
behaves over time.

This project brings these perspectives together by:

-   Extracting quarterly revenue data from financial webpages.
-   Retrieving historical stock market data programmatically.
-   Cleaning and processing the collected data with Pandas.
-   Calculating financial indicators such as moving averages and
    annualized volatility.
-   Visualizing financial trends through an interactive dashboard.

## Live Dashboard

**[Open Financial Performance
Dashboard](https://financial-dashboard-tokaaraafat.streamlit.app/)**

------------------------------------------------------------------------

## Key Features

### 1. Financial Data Collection

-   Extracts quarterly revenue information using **BeautifulSoup**.
-   Retrieves historical stock market data using **yfinance**.
-   Combines data from different sources for further analysis.

### 2. Data Processing & Analysis

Uses **Pandas** to organize, transform, and analyze financial datasets.

The analysis includes:

-   Quarterly revenue trends.
-   Historical stock price movements.
-   50-day Simple Moving Average (SMA).
-   Annualized stock volatility.

### 3. Interactive Dashboard

Built with **Streamlit** and **Plotly**, the dashboard provides
interactive financial visualizations and metrics exploration.

-   Explore financial trends through interactive charts.
-   Compare quarterly revenue with stock market performance.
-   Examine historical price movements and calculated indicators.

------------------------------------------------------------------------

## Technology Stack

  Technology      Purpose
  --------------- -----------------------------------------------
  Python          Main programming language
  Pandas          Data cleaning, manipulation, and analysis
  BeautifulSoup   Web scraping and quarterly revenue extraction
  yfinance        Historical stock market data retrieval
  Streamlit       Interactive dashboard development
  Plotly          Interactive data visualization

---

## Project Workflow

```text
Financial Webpages          Yahoo Finance
        |                         |
        v                         v
  BeautifulSoup                yfinance
        |                         |
        v                         v
 Quarterly Revenue       Historical Stock Data
        |                         |
        +------------+------------+
                     |
                     v
              Data Processing
                  Pandas
                     |
                     v
             Financial Analysis
          SMA & Annualized Volatility
                     |
                     v
           Interactive Dashboard
              Streamlit + Plotly
```

---

## Author

**Toka Raafat**

[GitHub](https://github.com/tokaaraafat)

---

*An applied Python project exploring financial data collection, analysis, and interactive visualization.*
