#!/bin/python

class Solution:
	def combinationSum_re(self, S, n, start, valueList):
		if n == 0:
			return self.ret.append(valueList)
		l = len(S)
		for i in range(start, l):
			if S[i] > n:
				return
			self.combinationSum_re(S, n-S[i], i, valueList + [S[i]])

	def combinationSum(self, S, n):
		"""
		:type S: List[int]
		:type n: int
		:rtype: List[List[int]]
		"""
		S.sort()
		self.ret = []
		self.combinationSum_re(S, n, 0, [])
		return self.ret

test = Solution()
S = [2, 3, 6, 7]
n = 7
print test.combinationSum(S, n)
