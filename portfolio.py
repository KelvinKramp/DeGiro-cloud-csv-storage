# copied from https://github.com/claudiocama/youtube/blob/master/2020-09-12%20-%20Api%20per%20Degiro/degiro.py#L26
import requests, json
import os

def get_cashfund():
    # Parte 1
    ## Recupero username e password da un file di configurazione
    ## Effettuo il login ed ottengo un sessionID
    URL_LOGIN = "https://trader.degiro.nl/login/secure/login"
    payload = {'username': os.environ.get('DEGIRO_USER'),
                       'password': os.environ.get('DEGIRO_PASSWORD'),
                       'isPassCodeReset': False,
                       'isRedirectToMobile': False}
    header = {'content-type': 'application/json'}
    r = requests.post(URL_LOGIN, headers=header, data=json.dumps(payload))
    print(r)
    sessionID = r.json()["sessionId"]

    ## Recupero l'intAccount
    URL_CLIENT = 'https://trader.degiro.nl/pa/secure/client'
    payload = {'sessionId': sessionID}
    r = requests.get(URL_CLIENT, params=payload)
    intAccount = r.json()["data"]["intAccount"]
    # Parte 2
    ## Recupero tutti i dati
    URL = "https://trader.degiro.nl/trading/secure/v5/update/"+str(intAccount)+";jsessionid="+sessionID
    payload = {'intAccount': intAccount,
               'sessionId': sessionID,
               'cashFunds': 0,
               'orders': 0,
               'portfolio': 0,
               'totalPortfolio': 0,
               'historicalOrders': 0,
               'transactions': 0,
               'alerts': 0}
    r = requests.get(URL, params=payload)
    data = r.json()

    ## Recupero i fondi dell'account
    cashfund = {}
    for currency in data["cashFunds"]["value"]:
        for parameter in currency["value"]:
            if parameter["name"] == "currencyCode":
                code = parameter["value"]
            if parameter["name"] == "value":
                value = parameter["value"]
        cashfund[code] = value

    cashfund = cashfund['EUR']

    return cashfund