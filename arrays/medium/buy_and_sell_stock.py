"""brute force (doesn't work for large elements"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0

    n = len(prices)
    for i in range(0, n):


        for j in range(i + 1, n):
            profit = prices[j] - prices[i]

            max_profit = max(profit, max_profit)

    return max_profit



"""optimal"""


def maxProfit_op( prices: List[int]) -> int:
    max_profit = 0
    mini = float("inf")
    n = len(prices)

    for price in prices:
        if price < mini:
            mini = price
        elif price - mini > max_profit:
            max_profit = price - mini

    return max_profit