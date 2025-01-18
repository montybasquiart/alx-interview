#!/usr/bin/python3
"""
Function to determine the minimum number of coins needed to meet a given amount
"""


def makeChange(coins, amount):
    """
    Determine the minimum number of coins needed to meet a given amount.
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
