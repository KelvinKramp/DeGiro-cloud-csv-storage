import degiroapi # uses requests as a dependency so dont forget to install requests
import json
import os
import yfinance as yf
from currency_converter import CurrencyConverter
c = CurrencyConverter()

# CREATE DEGIRO CLASS METHOD OBJECT
degiro = degiroapi.DeGiro()

# DEGIRO LOGIN FUNCTION
def degiro_login():
    # LOGIN
    username = os.environ.get("DEGIRO_USER")
    password = os.environ.get("DEGIRO_PASSWORD")
    degiro.login(username, password)

# GET PORTFOLIO FUNCTION
def portfolio():
    # DEGIRO LOGIN
    degiro_login()

    # TRANSFORM PORTOFOLIO INTO DICTIONARY FOR CHECKING
    portfolio = degiro.getdata(degiroapi.Data.Type.PORTFOLIO, True)
    portfolio_dict = {}
    for data in portfolio:
        if data['id'] != '15694498' and data['id'] != '15694501' and data['id'] != 'EUR':
            product_info = degiro.product_info(data['id'])
            portfolio_dict[product_info['symbol']] = (
            (product_info['name']), data['size'], (product_info['symbol']), (data['price']), (data['breakEvenPrice']))

    value_stock = []
    for i in portfolio_dict:
        value_stock.append(portfolio_dict[i][3])
    value_stock = sum(value_stock) # sum wallet in dollar
    value_stock = c.convert(value_stock, 'USD')

    return portfolio_dict, value_stock



# TRANSFORM PORTFOLIO INTO A TICKERS DICTIONARY
def transform_portfolio_into_tickers_dict(portfolio):
    tickers = {}
    for i in portfolio:
        tickers[i] = (portfolio[i][1], portfolio[i][-1])
    tickers = list(tickers)
    return tickers

# GET CURRENT PRICE OF TICKER
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


