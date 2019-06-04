from contextlib import closing

from bs4 import BeautifulSoup
from requests import get

def is_good_response(response):
    """Check if the given url appears to be an html doctype and check the
    status code returned with the response.
    """
    return(response.status_code == 200,
           response.text.find('html'))


def get_url(url):
    """Get the page's html code."""
    # return the reponse as a block of text, and close the connection
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    with closing(get(url, headers=headers, stream=True)) as response:
        if is_good_response(response):
            response.encoding = "utf-8"
            return response.text
        else:
            print('Invalid data.')


def scrap_official_site(prices):
    """Get the headset's price from the official shop."""
    print("Getting the official site's price...")
    domain = 'https://www.oculus.com/rift-s/'
    soup = BeautifulSoup(get_url(domain), 'lxml')
    price = soup.find('span', class_='_7w4l').text
    prices[domain] = float(price[1:])


def scrap_amazon(prices):
    """Get the headset's price from amazon.de"""
    print("Getting the amazon.de price...")
    domain = 'https://www.amazon.de/dp/B07PTMKYS7'
    soup = BeautifulSoup(get_url(domain), 'html.parser')
    price = soup.find('span', class_='a-size-medium a-color-price priceBlockBuyingPriceString').text.replace(',', '.')
    prices[domain] = float(price[4:])