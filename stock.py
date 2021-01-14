import yfinance as yf
import streamlit as st
from get_all_tickers import get_tickers as gt
import datetime

list_of_tickers = gt.get_tickers()

st.write("""# Stock Viewer App""")

# getting the company user selected
company = st.selectbox('Please select a stock', list_of_tickers)
tickerSymbol = company
tickerData = yf.Ticker(tickerSymbol)

# start and end dates for stock graphs
start = datetime.datetime(2005, 1, 1)
today = datetime.date.today()
start_date = st.date_input('Start date', start)
end_date = st.date_input('End date', today)

# error handling for dates
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

st.write('## Closing Price')
st.line_chart(tickerDf.Close) # closing price chart
st.write('## Volume Price')
st.line_chart(tickerDf.Volume) # volume price chart