import GraphFunctions as Gf
import yfinance as yf
import AnalysisModule as As
import datetime

print(datetime.date.today())
for days_in_past in range(100, 0, -1):
    last_day = datetime.date.today() + datetime.timedelta(days=-days_in_past)
    first_day = last_day  + datetime.timedelta(days=-60)
    stock_data = yf.download("AAPL", start=first_day, end=last_day, interval="1d")
    if As.macd_potential_buy(stock_data):
        Gf.draw_macd_buy(stock_data, "AAPL")

stock_data = yf.download("AAPL", period="6mo", interval="1d")
print(stock_data)
print(As.macd_potential_buy(stock_data))
Gf.draw_macd_buy(stock_data, "AAPL")
