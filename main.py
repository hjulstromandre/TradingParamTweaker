import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import statistics


tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
df = tickerData.history(period='1d', start='2013-01-01', end='2023-12-31')
print(df['Close'])
df = df.reset_index()


windowsize = 50
standarddeviations = 1

df['Moving average'] = df['Close'].rolling(window=windowsize).mean()

def generatebollingerbands():
    for i in range(len(df['Close']) - windowsize + 1):
        window = df['Close'][i : i + windowsize]
        window_average = sum(window) / windowsize
        std_dev = statistics.stdev(window)
        df.loc[i + windowsize - 1, 'Upper band'] = window_average + standarddeviations*std_dev
        df.loc[i + windowsize - 1, 'Lower band'] = window_average - standarddeviations*std_dev

generatebollingerbands()

fig = px.line(x=df['Date'], y=df['Close'])
fig.add_trace(go.Scatter(x=df['Date'], y=df['Moving average'], mode='lines', name='Moving average'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Upper band'], mode='lines', name='Upper band'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Lower band'], mode='lines', name='Lower band'))
fig.write_html("stock_plot.html")
#fig.show()

bank = 10000
startbank = bank
portfolio = 0


