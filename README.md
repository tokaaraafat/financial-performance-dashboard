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

```{=html}
<p>
```
Explore the deployed application:
```{=html}
</p>
```
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

## Financial Metrics

  -----------------------------------------------------------------------
  Metric                              Description
  ----------------------------------- -----------------------------------
  Quarterly Revenue                   Revenue reported by a company for
                                      each financial quarter

  50-Day Simple Moving Average (SMA)  Average closing price over the
                                      previous 50 trading days

  Annualized Volatility               A measure of the variability of
                                      stock returns, annualized to
                                      represent a yearly scale
  -----------------------------------------------------------------------

### Calculation Notes

**50-Day SMA**

The 50-day Simple Moving Average is calculated from the closing price:

``` python
sma_50 = closing_prices.rolling(window=50).mean()
```

**Annualized Volatility**

Annualized volatility is commonly calculated from the standard deviation
of daily returns:

``` python
daily_returns = closing_prices.pct_change()
annualized_volatility = daily_returns.std() * (252 ** 0.5)
```

The annualization factor of 252 represents the approximate number of
trading days in a year. These formulas describe the standard
calculations; refer to the implementation in the source code for the
exact behavior used by the application.

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

------------------------------------------------------------------------

## Project Workflow

``` text
Financial Webpages          Yahoo Finance
       |                         |
       v                         v
 BeautifulSoup                 yfinance
       |                         |
       v                         v
 Quarterly Revenue        Historical Stock Data
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
------------------------------------------------------------------------

## Skills Demonstrated

This project demonstrates practical experience with:

-   **Python programming:** Building a data-focused application and
    working with external data sources.
-   **Web scraping:** Extracting structured financial information from
    webpages using BeautifulSoup.
-   **API-based data retrieval:** Collecting historical market data
    through yfinance.
-   **Data cleaning and manipulation:** Preparing and organizing
    datasets with Pandas.
-   **Financial data analysis:** Calculating moving averages and stock
    volatility.
-   **Data visualization:** Building interactive charts with Plotly.
-   **Dashboard development:** Bringing data collection, analysis, and
    visualization together using Streamlit.
------------------------------------------------------------------------

## Author

**Toka Raafat**

[GitHub](https://github.com/tokaaraafat)

------------------------------------------------------------------------

*An applied Python project exploring financial data collection,
analysis, and interactive visualization.*
