#!/bin/python

class Solution:
	def palindromeNumber(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x < 0 or (x != 0 and x%10 == 0):
			return False

		tmp = x
		y = 0
		while tmp:
			y = y*10 + tmp%10
			tmp = tmp/10
		return y==x or y/10==x

	def palindromeNumber2(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x < 0 or (x != 0 and x%10 == 0):
			return False

		digit = 1
		tmp = x

		while tmp>=10:
			tmp = tmp/10
			digit = digit*10

		while x >= 10:
			left = x/digit
			right = x%10
			if left != right:
				return False
			x = (x%digit)/10
			digit = digit/100

		return True



test = Solution()

print test.palindromeNumber2(0)
print test.palindromeNumber2(111)
print test.palindromeNumber2(11111)
print test.palindromeNumber2(111111)
print test.palindromeNumber2(11211)
print test.palindromeNumber2(12311)
print test.palindromeNumber2(12321)
