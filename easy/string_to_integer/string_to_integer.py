#!/bin/python

class Solution():
	def stringToInteger(self, s):
		"""
		:type s: string
		:rtype: int
		"""
		INT_MAX = 2147483647
		flag = 1
		res = 0
		i = 0


		if s == "":
			return 0

		while i < len(s) and s[i].isspace():
			i += 1

		if i < len(s) and s[i] == '-':
			flag = -1
		if i < len(s) and (s[i] == '-' or s[i] == '+'):
			i += 1

		while i < len(s):
			if not s[i].isdigit():
				return 0
			if INT_MAX/10 > res and (INT_MAX - res*10 > int(s[i])):
				res = res*10 + int(s[i])
			else:
				return flag*INT_MAX
			i += 1

		res *= flag
		return res

#test = Solution()
#print test.stringToInteger("-1234")
#print test.stringToInteger("1234")
#print test.stringToInteger("1x234")
#print test.stringToInteger("  123")
#print test.stringToInteger("  -12312323234234")
