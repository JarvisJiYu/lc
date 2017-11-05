#!/bin/python

class Solution:
	def strStr(self, haystack, needle):
		"""
		:type haystack: string
		:type needle: string
		:type: int
		"""

		i = 0
		while i < (len(haystack) - len(needle) + 1):
			if haystack[i:i+len(needle)] == needle:
				return i
			i += 1

		return -1

#test = Solution()
#print test.strStr("abcdef", "cdef")
