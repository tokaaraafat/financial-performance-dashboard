# Financial Performance Visualizer & Analytics Dashboard

An end-to-end Python pipeline and interactive dashboard that analyzes the relationship between corporate financial metrics ( quarterly revenue) and stock market movements.

## Features
- **Automated Data Extraction:** Scrapes quarterly earnings data using `BeautifulSoup` and pulls market prices via `yfinance`.
- **Financial Analytics:** Computes 50-day moving averages (SMA) and annualized stock volatility using `pandas`.
- **Interactive Dashboard:** Built with `Streamlit` and `Plotly` for dynamic charting and metrics exploration.
- 
## Live Application & Code
[View Live Streamlit Dashboard](https://financial-dashboard-tokaaraafat.streamlit.app/)

## Setup & Execution
```bash
pip install -r requirements.txt
streamlit run app.py


