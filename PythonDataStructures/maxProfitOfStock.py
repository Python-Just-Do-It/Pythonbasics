import sys

def maxProfit(prices):
        leastPrice = sys.maxsize
        profit = 0
        for price in prices:
            gain = price - leastPrice
            if gain > profit:
                profit = gain
            if price < leastPrice:
                leastPrice = price
        return profit

print(maxProfit([7,1,5,3,6,4]))