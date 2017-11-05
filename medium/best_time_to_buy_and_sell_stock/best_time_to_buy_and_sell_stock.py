#!/bin/python

class Solution:
	def bestTimeToBuyAndSellStock(self, price):
		"""
		:type price: List[int]
		:rtype: int
		"""
		buy_price = price[0]
		profit = 0

		for i in range(1, len(price)):
			buy_price = min(buy_price, price[i])
			profit = max(profit, price[i] - buy_price)
		return profit

test = Solution()
price = [3, 2, 1.2, 2.2, 3, 7, 5, 18, 4, 6]

print test.bestTimeToBuyAndSellStock(price)
