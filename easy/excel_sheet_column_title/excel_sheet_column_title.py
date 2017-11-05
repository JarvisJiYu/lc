#!/bin/python

class Solution:
	def excelSheetColumnTitle(self, n):
		"""
		:type number: int
		:rtype: string
		"""
		res = ''
		while n:
			res = chr((n-1)%26 + 65) + res
			n = (n-1)/26

		return res


#test = Solution()
#print test.excelSheetColumnTitle(703)
