import numpy as np
import tulipy as ti
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# looks for a rise in the mach histogram and a positive zero crossing between the last 2 values
def macd_potential_buy(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    macd1, macd2, macdhistogram = ti.macd(numpyclose, 8, 17, 9)  # for buy signals it should be 8,17,9

    if macdhistogram[-1] > 0 > macdhistogram[-2] and \
            macdhistogram[-1] >= macdhistogram[-2] >= macdhistogram[-3] >= macdhistogram[-4]:
        return True
    else:
        return False


# looks for a rise in the mach histogram and a negative zero crossing between the last 2 values
def macd_potential_sell(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    macd1, macd2, macdhistogram = ti.macd(numpyclose, 12, 26, 9)  # for sell signals it should be 12, 26, 9

    if macdhistogram[-1] < 0 < macdhistogram[-2] and \
            macdhistogram[-1] <= macdhistogram[-2] <= macdhistogram[-3] <= macdhistogram[-4]:
        return True
    else:
        return False


def sma_potential_buy(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    sma = ti.sma(numpyclose, 17)
    if sma[-50] < sma[-5] < sma[-1] < closing_price_list[-1] and closing_price_list[-2] < sma[-2]:
        return True
    else:
        return False


def sma_potential_sell(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    sma = ti.sma(numpyclose, 26)
    if sma[-50] > sma[-5] > sma[-1] > closing_price_list[-1] and closing_price_list[-2] > sma[-2]:
        return True
    else:
        return False


# checks if today is a positive value
def is_today_rising(stock):
    current_value = stock['Close'].tolist()[-1]
    open_value = stock['Open'].tolist()[-1]
    if current_value >= open_value:
        return True
    else:
        return False


# checks if today is a negative value
def is_today_falling(stock):
    current_value = stock['Close'].tolist()[-1]
    open_value = stock['Open'].tolist()[-1]
    if current_value <= open_value:
        return True
    else:
        return False


# returns open close values of last day in stock
def return_open_close(stock):
    current_value = stock['Close'].tolist()[-1]
    open_value = stock['Open'].tolist()[-1]
    return [open_value, current_value]


# returns open close values of first day in stock
def return_open_close_first_day(stock):
    current_value = stock['Close'].tolist()[0]
    open_value = stock['Open'].tolist()[0]
    return [open_value, current_value]


# returns the latest 10 macd histogram of the stock and closing prices for sell
def return_macd_histogram_and_closing_prices_sell(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    macd1, macd2, macdhistogram = ti.macd(numpyclose, 12, 26, 9)  # for sell signals it should be 12, 26, 9

    return [list(macdhistogram)[-10:], closing_price_list[-10:]]


# returns the latest 10 macd histogram of the stock and closing prices for buy
def return_macd_histogram_and_closing_prices_buy(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    macd1, macd2, macdhistogram = ti.macd(numpyclose, 8, 17, 9)  # for sell signals it should be 12, 26, 9

    return [list(macdhistogram)[-10:], closing_price_list[-10:]]


# returns the latest 10 sma of the stock and closing prices for sell
def return_sma_and_closing_prices_sell(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    sma = ti.sma(numpyclose, 26)
    return [list(sma)[-10:], closing_price_list[-10:]]


# returns the latest 10 sma of the stock and closing prices for buy
def return_sma_and_closing_prices_buy(stock):
    closing_price_list = stock['Close'].tolist()
    numpyclose = np.asarray(closing_price_list)
    sma = ti.sma(numpyclose, 17)
    return [list(sma)[-10:], closing_price_list[-10:]]

#  This is how a stock looks like after gets out of the yfinance
#               Open    High     Low   Close    Volume  Dividends  Stock Splits
# Date
# 2019-03-05  110.78  110.92  109.78  110.24  19538300        0.0             0
# 2019-03-06  110.41  111.19  109.97  110.29  17687000        0.0             0
# 2019-03-07  109.95  110.09  108.44  108.95  25339000        0.0             0
# 2019-03-08  107.73  109.26  107.38  109.07  22818400        0.0             0
# 2019-03-11  109.54  111.48  109.53  111.36  26491600        0.0             0
# ...            ...     ...     ...     ...       ...        ...           ...
# 2020-02-27  163.32  167.03  157.98  158.18  93174900        0.0             0
