#!/bin/python

class Solution:
	def romanToInteger(self, r):
		"""
		:type r: string
		:rtype: int
		"""
		numerals = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

		rr = r[::-1]
		print rr

		sum = 0
		last = None
		for i in range(0, len(rr)):
			if last and numerals[rr[i]] < last:
				sum -= 2*numerals[rr[i]]
			
			sum += numerals[rr[i]]
			last = numerals[rr[i]]

		return sum

test = Solution()
print test.romanToInteger("IV")
