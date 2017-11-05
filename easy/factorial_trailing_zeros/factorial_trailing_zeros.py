#!/bin/python

class Solution:
	def factorialTrailingZeros(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		res = 0
		while n > 0:
			n = n/5
			res += n

		return res

#test = Solution()
#print test.factorialTrailingZeros(135)
