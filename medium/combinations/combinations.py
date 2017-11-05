#!/bin/python

class Solution:
	def combinations_dfs1(self, n, k):
		res = []
		if n == k+1:
			tmp = []
			for i in range(1, n):
				tmp += [i]
			res = [tmp]
			res = [[1,2]]
			print n, res
			return res

		res = self.combinations_dfs1(n-1, k)
		print n, res
		l = len(res)
		for i in range(l):
			tmp1 = res[i][:]
			tmp1[-1] = n - 1
			res += [tmp1]
		return res
	def combinations_dfs2(self, n, k, start):
		res = []
		if start == n - k +1:
			tmp = []
			for i in range(start, n+1):
				tmp += [i]
			res = [tmp]
			return res

		res = self.combinations_dfs2(n, k, start+1)
		print n, res
		l = len(res)
		for i in range(l):
			tmp1 = res[i][:]
			tmp1[-1] = start
			res += [tmp1]
		return res

	def combinations_dfs(self, n, k, res):
		if n == k+1:
			tmp = []
			for i in range(1, n):
				tmp += [i]
			res = [tmp]
			res = [[1,2]]
			print n, res
			return

		self.combinations_dfs(n-1, k, res)
		print n, res
		l = len(res)
		for i in range(l):
			tmp1 = res[i]
			tmp1[-1] = n
			res += [tmp1]

	def combinations(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		res1 = []
		res2 = []
		aaa = []
		#self.combinations_dfs(n, k, res)
		res1 = self.combinations_dfs1(n, k)
		res2 = self.combinations_dfs2(n, k, 1)

		return res1+res2

test = Solution()

print test.combinations(4, 2)
