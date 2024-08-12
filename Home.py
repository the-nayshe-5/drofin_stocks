import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
import datetime

st.set_page_config(page_title="Home - DroFin",
                   layout="wide",
                   page_icon="💰")

def get_data(ticker, start_date, end_date, period):
    data = yf.download(ticker, start = start_date, end = end_date, interval = period)
    stocks = yf.Ticker(ticker)
    # st.write(data)
    col = st.selectbox('Select Option:', ["Open", "Close", "Adj Close"])
    fig1 = px.line(data, x = data.index, y = data[col], title = ticker + " Stocks")
    st.plotly_chart(fig1)
    return [data, stocks]

def get_info(data, stocks):
    with pricing_data:
        st.markdown("### Price Movements")
        st.dataframe(data)

    with balance_sheet:
        st.markdown("### Balance Sheet")
        st.dataframe(stocks.balance_sheet)

    with income_statement:
        st.markdown("### Income Statement")
        st.dataframe(stocks.income_stmt)

    with cash_flow:
        st.write("### Cash Flow")
        st.dataframe(stocks.cashflow)

    with other_info:
        st.write(f"Company: {stocks.info['longName']}")
        st.write(f"Sector: {stocks.info['sector']}")
        st.write(f"Industry: {stocks.info['industry']}")
        st.write(f"Market Cap: {stocks.info['marketCap']}")
        st.write(f"P/E Ratio: {stocks.info['trailingPE']}")

st.title("Welcome to Android Club Stocks Market! 📈")
ticker = st.sidebar.text_input('Enter your answer here:', value="AAPL")
start_date = datetime.date.today()-datetime.timedelta(days=1)
end_date = datetime.date.today()
period = "30m"


data, stocks = get_data(ticker, start_date, end_date, period)
pricing_data, balance_sheet, income_statement, cash_flow, other_info = st.tabs(["Pricing Data", "Balance Sheet", "Income Statement", 
                                                              "Cash Flow", "More Info"])
get_info(data, stocks)


# try:
#     data, stocks = get_data(ticker, start_date, end_date, period)
#     pricing_data, balance_sheet, income_statement, cash_flow, other_info = st.tabs(["Pricing Data", "Balance Sheet", "Income Statement", 
#                                                                   "Cash Flow", "More Info"])
#     get_info(data, stocks)
# except:
#     st.write("Enter Valid Details.")

