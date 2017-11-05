#!/bin/python

class Solution:
	def validParentheses(self, s):
		"""
		:type s: string
		:rtype: bool
		"""
		p = {"(":")", "{":"}", "[":"]"}

		stack = []
		for i in range(len(s)):
			if s[i] == '{' or s[i] == '(' or s[i] == '[':
				stack.append(s[i])
			elif s[i] == '}' or s[i] == ')' or s[i] == ']':
				if len(stack) == 0 or p[stack.pop()] != s[i]:
					return False
			else:
				return False

		if len(stack) != 0:
			print stack
			return False


		return True

#test = Solution()
#print test.validParentheses("[{{{()}}}]")
#print test.validParentheses("][{{{}()}}]")
