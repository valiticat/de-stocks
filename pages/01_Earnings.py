import streamlit as st
import yfinance as yf
import pandas as pd


st.subheader('')

jnj = yf.Ticker("JNJ")
st.header(jnj.info['longName'])
# EPS
eps_df = jnj.earnings_dates
st.text("Latest EPS reported vs estimate")
latest_eps = eps_df[eps_df['Reported EPS'].notnull()].head(1)
st.text(latest_eps.to_string(index=False))

data = yf.download('JNJ','2023-10-01','2023-10-20')['Close']
st.line_chart(data)

#data = yf.download(tickers_list,'2015-1-1')['Adj Close']