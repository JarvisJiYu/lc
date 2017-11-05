#!/bin/python

class Solution:
	def divideTwoIntegers(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		flag = (a < 0 and b > 0) or (a > 0 and b < 0)
		m = abs(a)
		n = abs(b)
		res = 0
		while m >= n:
			x = n
			i = 0
			while m >= x:
				m -= x
				res += (1<<i)
				i += 1
				x <<= i
		if flag:
			res = -res
		return min(max(-2147483648, res), 2147483647)

	def divideTwoIntegers_toolong(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		res = 0
		flag = (a < 0 and b > 0) or (a > 0 and b < 0)
		m = abs(a)
		n = abs(b)
		while m >= n:
			m = m - n
			res += 1

		if flag:
			if m != 0:
				res = -res-1
			else:
				res = -res

		return min(max(-2147483648, res), 2147483647)

test = Solution()
a = -130
b = 13
print test.divideTwoIntegers(a, b)
print test.divideTwoIntegers_toolong(a, b)
print a/b
