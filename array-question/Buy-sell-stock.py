# link for question --> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/






# Best Time to Buy and Sell Stock


# --------------------question statement-----------------
# you are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# -------------------solution---------------------
class Solution(object):
    def maxProfit(self, prices):
        
        min_price = float('inf') 
        max_profit = 0 
        
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit