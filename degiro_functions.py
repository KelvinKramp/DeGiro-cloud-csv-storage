import degiroapi # uses requests as a dependency so dont forget to install requests
import json
import os
import yfinance as yf

degiro = degiroapi.DeGiro()

def degiro_login():
    # OPEN CREDENTIAL FILE
    secrets_file_path = os.path.join("secrets.json")
    with open(secrets_file_path, "r") as read_file:
        read_file = read_file.read()
        data = json.loads(str(read_file))

    # LOGIN
    username = data["DEGIRO_USER"]
    password = data["DEGIRO_PASSWORD"]
    degiro.login(username, password)


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
        if data['id'] == '15694498':
            value_wallet = data['value']

    return portfolio_dict, value_wallet

def transform_portfolio_into_tickers_dict(portfolio):
    tickers = {}
    for i in portfolio:
        tickers[i] = (portfolio[i][1], portfolio[i][-1])
    tickers = list(tickers)
    return tickers

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


