import degiro_functions as degiro_f
import portfolio as pf
from datetime import datetime as dt
import csv
import os
import pathlib
import firebase_connection as fc
from apscheduler.schedulers.background import BackgroundScheduler

# create class instance
sched = BackgroundScheduler()
name_csv_file = "/YOUR_WALLET_NAME.csv"

def store_wallet():
    # define path of file
    cwd = os.path.dirname(os.path.realpath(__file__))
    file_path_wallet = cwd + name_csv_file

    # if file does not exist in path then create it
    file = pathlib.Path(file_path_wallet)
    if file.exists ():
        print(file_path_wallet)
    else:
        print ("Wallet file does not exist")
        print(file_path_wallet)
        # make csv file with column titles
        print("saving file as", file_path_wallet)
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

    print("Appended new row to csv file consisting of", dt.now(), cashfund, value_portfolio, tickers, price_tickers)
    # use firebase connection to store wallet csv under the same name on firebase cloud
    fc.store_on_firebase(file_path_wallet, name_csv_file)
    sched.print_jobs()

def start_working():
    sched.start()
    time_interval = int(os.environ.get('TIME-INTERVAL'))
    print("TIME-INTERVAL is set to: ", time_interval)
    sched.add_job(store_wallet, 'interval', minutes=time_interval, id='storing_job', next_run_time=dt.now())