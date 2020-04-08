"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
        best_without_stock: int = 0
        best_with_stock: int = float('-inf')
        
        for i in range(len(prices)):
            best_with_stock: int = max(best_with_stock, best_without_stock - prices[i])
            best_without_stock: int = max(best_without_stock, best_with_stock + prices[i])
        
        return best_without_stock
