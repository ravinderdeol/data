"""
The price of Bitcoin at each halving event in USD. And the change in price between each event.
"""

import datetime
import cryptocompare

## -- price of bitcoin at each halving event in usd -- ##

halving_one = format(cryptocompare.get_historical_price("btc", "usd", datetime.datetime(2012, 11, 28))["BTC"]["USD"], ".2f")
halving_two = format(cryptocompare.get_historical_price("btc", "usd", datetime.datetime(2016, 7, 9))["BTC"]["USD"], ".2f")
halving_three = format(cryptocompare.get_historical_price("btc", "usd", datetime.datetime(2020, 5, 11))["BTC"]["USD"], ".2f")

## -- calculate the price difference between each halving event as an integer -- ##

halving_two_halving_one_integer = format(float(halving_two) - float(halving_one), ".2f")
halving_three_halving_two_integer = format(float(halving_three) - float(halving_two), ".2f")

## -- calculate the price difference between each halving event as a percentage -- ##

halving_two_halving_one_percentage = format(((float(halving_two) - float(halving_one)) / float(halving_one)) * 100, ".2f")
halving_three_halving_two_percentage = format(((float(halving_three) - float(halving_two)) / float(halving_two)) * 100, ".2f")

## -- output the results in a readable format -- ##

first_halving_output = f"Bitcoin Halving #1 - 28 November 2012\nPrice: ${halving_one}\n"
second_halving_output = f"Bitcoin Halving #2 - 09 July 2016\nPrice: ${halving_two}\nChange: {halving_two_halving_one_percentage}% (${halving_two_halving_one_integer})\n"
third_halving_output = f"Bitcoin Halving #3 - 11 May 2020\nPrice: ${halving_three}\nChange: {halving_three_halving_two_percentage}% (${halving_three_halving_two_integer})"

print(first_halving_output)
print(second_halving_output)
print(third_halving_output)
