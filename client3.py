import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Corrected computation of price
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """Get ratio of price_a and price_b"""
    if price_b == 0:
        return None  # Handling division by zero
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    prices = {}  # Initialize prices dictionary
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Calculate and print the ratio using prices dictionary
        if "ABC" in prices and "DEF" in prices:
            ratio = getRatio(prices["ABC"], prices["DEF"])
            print("Ratio %s" % ratio)
