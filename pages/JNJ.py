import streamlit as st
import yfinance as yf
import pandas as pd

st.header('Johnson & Johnson (JNJ)')
st.subheader('')

jnj = yf.Ticker("JNJ")
# EPS
eps_df = jnj.earnings_dates
latest_eps = eps_df[eps_df['Reported EPS'].notnull()].head(1)
latest_eps
#f"Latest EPS reported: {latest_eps['Reported EPS']} USD. Estimate: USD"
#st.text(pd.to_datetime(ids).year)
#test = eps_df[pd.to_datetime(eps_df.index.dt.date) == '2023-10-17']
#test
#pd.to_datetime(mygrafic['Дата'].dt.date)

# get historical market data
hist = jnj.history(period="1mo")
st.line_chart(hist)
