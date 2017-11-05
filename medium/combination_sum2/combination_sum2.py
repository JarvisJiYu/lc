#!/bin/python

class Solution:
	def combinationSum_re(self, S, n, start, valueList):
		if n == 0:
			if valueList not in self.ret:
				return self.ret.append(valueList)
		l = len(S)

		for i in range(start, l):
			if S[i] > n:
				return
			#if S[i] in valueList:
			#	k = 1
			#	for j in valueList:
			#		if j == S[i]:
			#			k += 1
			#	if k > self.times[S[i]]:
			#		continue
			##if S[i] < 0:
			##	continue
			##new_S = S[:]
			##new_S[i] = -1
			##self.combinationSum_re(new_S, n-S[i], i, valueList + [S[i]])
			self.combinationSum_re(S, n-S[i], i+1, valueList + [S[i]])

	def combinationSum(self, S, n):
		"""
		:type S: List[int]
		:type n: int
		:rtype: List[List[int]]
		"""
		S.sort()
		self.ret = []
		#self.times = {}
		#for i in S:
		#	if i not in self.times:
		#		self.times[i] = 1
		#	else:
		#		self.times[i] += 1
		self.combinationSum_re(S, n, 0, [])
		return self.ret

test = Solution()
S = [10, 1, 2, 7, 6, 1, 5]
n = 8
print test.combinationSum(S, n)
