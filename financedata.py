import yfinance as yf
import matplotlib

microsoft = yf.Ticker('MSFT')

microsoft_data = microsoft.history(period= 'max')

microsoft_data.head()

# GRAPH.... 

# def make_graph(stock_data, revenue_data, stock):
#     fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
#     stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
#     revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
#     fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
#     fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
#     fig.update_xaxes(title_text="Date", row=1, col=1)
#     fig.update_xaxes(title_text="Date", row=2, col=1)
#     fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
#     fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
#     fig.update_layout(showlegend=False,
#     height=900,
#     title=stock,
#     xaxis_rangeslider_visible=True)
#     fig.show()