#!/bin/python

class Solution:
	def reverseInteger(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		new_x = 0
		flag = -1
		if x >= 0:
			flag = 1

		x = abs(x)

		while x:
			new_x = new_x*10 + x%10
			x = x/10

		new_x = new_x * flag
		if new_x < 2147483648 or new_x >= -2147483648:
			return new_x
		return 0

#test = Solution()
#print test.reverseInteger(0)
#print test.reverseInteger(1)
#print test.reverseInteger(113)
#print test.reverseInteger(123456789)
#print test.reverseInteger(2147483648)
#print test.reverseInteger(1000)
