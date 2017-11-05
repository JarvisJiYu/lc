#!/bin/python

class Solution:
	def lengthOfLastWord(self, n):
		"""
		:type n: string
		:rtype: int
		"""

		s = n.split(" ")
		return len(s[-1])

		return 0

#test = Solution()
#print test.lengthOfLastWord("hi world")
