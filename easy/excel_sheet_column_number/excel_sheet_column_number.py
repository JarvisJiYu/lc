#!/bin/python

class Solution:
	def excelSheetColumnNumber(self, title):
		"""
		:type title: string
		:rtype: int
		"""
		column = 0
#		l = len(title)
#		for i in range(0, l):
#			column += 26**(i)*(ord(title[l-i-1])-ord('A')+1)
		for c in title:
			column = column*26 + (ord(c)-(ord('A')-1))

		return column

test = Solution()
print test.excelSheetColumnNumber("AA")
print test.excelSheetColumnNumber("AZ")
print test.excelSheetColumnNumber("BZ")
print test.excelSheetColumnNumber("YZ")
print test.excelSheetColumnNumber("ZZ")
print test.excelSheetColumnNumber("AAA")
