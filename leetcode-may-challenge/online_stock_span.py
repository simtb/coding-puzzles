"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
"""

from typing import List

#Dynamic programming
class StockSpanner:

    def __init__(self):
        self.prices: List[int] = []
        self.tmp: List[int] = []
        self.max_price: int = float('-inf')
        self.size: int = 0
        
    def next(self, price: int) -> int:
        span: int = 0
        if self.prices == []:
            span: int = 1
        elif price >= self.max_price:
            span: int = self.size + 1
        else:
            yesterday_price: int = self.prices[-1]
            if price < yesterday_price:
                span: int = 1
            else:
                current_span: int = 1
                i: int = self.size - 1
                while True:
                    if i < 0:
                        break
                    if price >= self.prices[i]:
                        current_span += self.tmp[i]
                        i -= self.tmp[i]
                    else:
                        break
                span: int = current_span
        
        self.prices.append(price)
        self.size += 1
        self.max_price: int = max(self.max_price, price)
        self.tmp.append(span)
        
        return span

#Stack solution
class StockSpanner:

    def __init__(self):
        self.stack: List[int] = []
        

    def next(self, price: int) -> int:
        span: int = 1
        while(self.stack and price >= self.stack[-1][0]):
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

         
