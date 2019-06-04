import json
from sys import exit

from functions import scrap_official_site, scrap_amazon
from mailing import send_prices

prices = dict()

if __name__ == '__main__':
    scrap_official_site(prices)
    scrap_amazon(prices)

    with open('prices.json', 'w') as f:
        json.dump(prices, f)

    for price in prices.values():
        if float(price) <= 449.0:
            send_prices(prices)
            exit(0)

