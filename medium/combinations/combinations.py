#!/bin/python

class Solution:
	def combinations_dfs(self, n, k, start, valueList):
		if self.count == k:
			self.res.append(valueList)
			return

		for i in range(start, n+1):
			self.count += 1
			self.combinations_dfs(n, k, i+1, valueList + [i])
			self.count -= 1

	def combinations(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		self.res = []
		self.count = 0
		self.combinations_dfs(n, k, 1, [])

		return self.res

test = Solution()

print test.combinations(7, 3)
