import streamlit as st
import yfinance as yf

jnj = yf.Ticker("JNJ")

# get historical market data
hist = jnj.history(period="1mo")
