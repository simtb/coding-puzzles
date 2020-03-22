"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

from typing import List

def solution(stocks: List[int]) -> int:
    number_of_stocks: int = len(stocks)
    if number_of_stocks == 0:
        return 
    elif number_of_stocks == 1:
        return stocks[0]
    
    max_stock_price: int = stocks[0]
    min_stock_price: int = stocks[0]
    maximum_profit: int = 0

    for i in range(1, number_of_stocks):
        current_stock_price: int = stocks[i]
        if current_stock_price > max_stock_price:
            max_stock_price: int = current_stock_price
        if current_stock_price < min_stock_price: 
            profit: int = max_stock_price - min_stock_price
            if profit > maximum_profit:
                maximum_profit: int = profit
            max_stock_price: int = current_stock_price
            min_stock_price: int = current_stock_price

        profit: int = max_stock_price - min_stock_price
        if profit > maximum_profit:
            maximum_profit: int = profit
        
    return maximum_profit
