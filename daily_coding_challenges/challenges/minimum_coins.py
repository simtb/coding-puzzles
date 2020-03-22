"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

from typing import List

def minimum_coins(amount: int) -> int:
    currency_denominations: List[int] = [25, 10, 5, 1]

    if amount <= 0: 
        return None

    current_amount: int = amount
    number_of_denominations: int = len(currency_denominations)
    number_of_coins: int = 0

    for i in range(number_of_denominations):
        currency_denomination = currency_denominations[i]

        while True:

            remaining_amount: int = current_amount - currency_denomination

            if remaining_amount < 0:
                break
            else:
                number_of_coins: int = number_of_coins + 1
                current_amount: int = remaining_amount

        if current_amount == 0:
            return number_of_coins
