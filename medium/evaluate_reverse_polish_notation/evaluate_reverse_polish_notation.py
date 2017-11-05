#!/bin/python

class Solution:
	def doCompute(self, a, b, op):
		if op == "+":
			return a+b
		if op == "-":
			return a-b
		if op == "*":
			return a*b
		if op == "/":
			print a,b
			print a/b
			if a*b < 0:
				return (-(-a)/b)
			return a/b

	def evaluateReversePolishNotation(self, S):
		"""
		:type S: List[]
		:rtype: int
		"""
		stack = []

		for i in range(0, len(S)):
			print stack
			if S[i].isdigit():
				stack.append(int(S[i]))
			else:
				a = stack.pop()
				b = stack.pop()
				stack.append(self.doCompute(b, a, S[i]))

		return stack.pop()

test = Solution()
S = ["4", "13", "5", "/", "+"]
print test.evaluateReversePolishNotation(S)
