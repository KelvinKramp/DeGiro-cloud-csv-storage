import degiro_functions as degiro_f
import portfolio as pf
from datetime import datetime as dt
import csv
import os
import pathlib

# define path of file
file_path_wallet = os.path.join("data_wallet.csv")

# if file does not exist in path then creat it
file = pathlib.Path("data_wallet.csv")
if file.exists ():
    print ("Wallet file exists")
else:
    print ("Wallet file does not exist")
    # make csv file with column titles
    with open(file_path_wallet, mode='w') as table1:
        csv_writer = csv.writer(table1, delimiter=',')
        csv_writer.writerow(["date", "cashfund", "total money", 'tickers', 'price stock'])

# get cashfunds out of portfolio
cashfund = pf.get_cashfund()

# get total value of portofolio
portfolio_dict, value_portfolio = degiro_f.portfolio()

# get stocksymbols from portfolio
tickers = degiro_f.transform_portfolio_into_tickers_dict(portfolio_dict)

# get prices of tickers
price_tickers = []
for i in tickers:
    price_tickers.append(degiro_f.get_current_price(i))

# append money in portfolio, total price stock, sum of first two, number of stock and list and store stockssymbols info in csv file
with open(file_path_wallet, mode='a') as table:
    csv_writer = csv.writer(table, delimiter=',')
    csv_writer.writerow([dt.now(), cashfund, value_portfolio, tickers, price_tickers])
