"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0 for i in range(amount + 1)]
        ways[0] = 1 #because for 0 amount, we can have 1 way ie by not using any coin
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    ways[i] = ways[i] + ways[i - coin] #main formula
        return ways[-1] #last value in ways array
