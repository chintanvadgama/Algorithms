# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

import sys
# 1. With multiple Transaction
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        if len(set(prices)) == 1 and len(prices) != 1:
            return 0
        i = 0
        j = 1
        # maximum = []
        total = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total

    def singleTransactionMaxProfit(self,prices):
        if len(prices) < 2:
            return 0
        if len(set(prices)) == 1 and len(prices) != 1:
            return 0
        maxProfilt = 0
        buy = 0
        for sell in range(len(prices) - 1):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxProfilt = max(prices[sell] - prices[buy],maxProfilt)
            print("prices[%s]=%s,prices[%s]=%s,maxProfit=%s" % (sell, prices[sell], buy, prices[buy],maxProfilt))
        return maxProfilt

# 2. With single transaction allowed

print(Solution().singleTransactionMaxProfit([7,1,5,3,6,4]))