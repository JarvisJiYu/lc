#!/bin/python

class Solution:
	def longestCommonPrefix(self, strs):
		"""
		:type strs: array
		:rtype: string
		"""
		if strs == []:
			return ""

		array_len = len(a)
		res = ""
		j = 0

		while True:
			for i in range(0, array_len):
				if len(strs[i]) <= j:
					return res
				if strs[i][j] != strs[0][j]:
					return res
			
			res += strs[0][j]
			j += 1

#test = Solution()
#a = ["", "abcdefg", "abcddd", "abcdxx", "aa"]
#print test.longestCommonPrefix(a);
