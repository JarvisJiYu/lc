#!/bin/python

class Solution:
	def zigzagConversion(self, s, num):
		"""
		:type s: string
		:type num: int
		:rtype: string
		"""

		i = 0
		j = 0
		first = 0
		flag = 0
		new_s = ['' for k in range(num)]
		for c in s:
			if flag == 0:
				new_s[i%num] += c
				if (i+1)%num == 0:
					flag = 1
				i += 1
			else:
				new_s[num/2] += c
				flag = 0

		res = []
		for i in range(num):
			res += new_s[i]

		return res

test = Solution()
print test.zigzagConversion("abcdefgh", 3)
print test.zigzagConversion("abcdefghi", 3)
print test.zigzagConversion("abcdefghij", 3)
print test.zigzagConversion("abcdefghijk", 3)
