"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i]
is the price of a given stock on the ith day.

You want to maximize your profit by choosing a
single day to buy one stock and choosing a different
day in the future to sell that stock.

Return the maximum profit you can achieve from
this transaction. If you cannot achieve any profit,
return 0.
"""

def maxProfit(prices):
    profits = []
    for index in range(len(prices)):
        buy = prices[index]
        if index == len(prices)-1:
            break
        sell = max( prices[index+1:])
        profit = sell - buy
        if profit < 0:
            profits.append(0)
        else:
            profits.append(profit)
    return max(profits)

# First iteration - Too slow, too many loops and checks

result = maxProfit(prices =[7,1,5,3,6,4])
print(result)