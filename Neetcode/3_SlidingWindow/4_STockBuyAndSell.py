"""
LC121 :Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Explore:
->> can the array be empty : yes

Brainstorm:
-> using Two Loops : O(N)^2
-> using sigle Iteration : Time = O(n)

Approach:
-> Iterate through the array
-> store the min value
-> if you find value greater than the min value at alter day ,save the profit
-> fidn the max profit
-> return the answr




"""


class Solution:
    def maxProfit(self, prices) -> int:
        L = 0
        min_price = float("inf")
        max_profit = float("-inf")

        for key, value in enumerate(prices):

            if value < min_price:
                min_price = value
                L = key

            if value > min_price and key > L:
                max_profit = max(max_profit, value - prices[L])

        return 0 if max_profit == float("-inf") else max_profit























