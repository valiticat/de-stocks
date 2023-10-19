import streamlit as st
import yfinance as yf
import pandas as pd

st.header('Johnson & Johnson (JNJ)')
st.subheader('')

jnj = yf.Ticker("JNJ")

# get historical market data
hist = jnj.history(period="1mo")
st.line_chart(hist)
