import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
import datetime
#---------------------------------------------------#
    ## PAGE LAYOUT ##
#---------------------------------------------------#

st.set_page_config(page_title="Home - DroFin",
                   layout="wide",
                   page_icon="💰")

fin_periods = {"1 minute": "1m",
               "2 minutes" : "2m",
               "5 minutes": "5m",
               "15 minutes" : "15m",
               "30 minutes": "30m",
               "60 minutes" : "60m",
               "90 minutes": "90m",
               "1 hour" : "1h",
               "1 day" : "1d",
               "5 days" : "5d",
               "1 week" : "1wk",
               "1 month" : "1mo",
               "3 month" : "3mo"}

def get_data(ticker, start_date, end_date, period):
    data = yf.download(ticker, start = start_date, end = end_date, interval = period)
    stocks = yf.Ticker(ticker)
    # st.write(data)
    fig1 = px.line(data, x = data.index, y = data['Adj Close'], title = ticker + " Stocks")
    st.plotly_chart(fig1)
    return [data, stocks]

def get_info(data, stocks):
    with pricing_data:
        st.markdown("### Price Movements")
        st.write(data)

    with balance_sheet:
        st.markdown("### Balance Sheet")
        st.write(stocks.balance_sheet)

    with income_statement:
        st.markdown("### Income Statement")
        st.write(stocks.income_stmt)

    with cash_flow:
        st.write("### Cash Flow")
        st.write(stocks.cashflow)

    with other_info:
        st.write(f"Company: {stocks.info['longName']}")
        st.write(f"Sector: {stocks.info['sector']}")
        st.write(f"Industry: {stocks.info['industry']}")
        st.write(f"Market Cap: {stocks.info['marketCap']}")
        st.write(f"P/E Ratio: {stocks.info['trailingPE']}")

st.title("Welcome to DroFin App! 🤖")
ticker = st.sidebar.text_input('Ticker', value="AAPL")
start_date = st.sidebar.date_input('Start Date', value=datetime.date.today()-datetime.timedelta(days=1))
end_date = st.sidebar.date_input('End Date')
period = st.sidebar.selectbox('Select Period', list(fin_periods.keys()))

try:
    data, stocks = get_data(ticker, start_date, end_date, fin_periods[period])
    pricing_data, balance_sheet, income_statement, cash_flow, other_info = st.tabs(["Pricing Data", "Balance Sheet", "Income Statement", 
                                                                  "Cash Flow", "More Info"])
    get_info(data, stocks)
except:
    st.write("Enter Valid Details.")

