#!/bin/python

class Solution:
	def bestTimeToBuyAndSellStock2(self, S):
		"""
		:type S: List[int]
		:rtype: int
		"""
		profit = 0
		i = 1
		while i < len(S):
			if S[i] > S[i-1]:
				profit += S[i] - S[i-1]
			i += 1

		return profit

test = Solution()
S = [1, 3, 5, 7, 4, 3, 2, 5, 3, 5, 3]
print test.bestTimeToBuyAndSellStock2(S)
