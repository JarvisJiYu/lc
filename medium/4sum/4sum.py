#!/bin/python

class Solution:
	def a4Sum(self, S, n):
		"""
		:type S: List[int]
		:type n: int
		:rtype: List[List[int]]
		"""
		l = len(S)
		res = set()
		d = {}
		S.sort()

		i = 0
		j = 0

		for i in range(l):
			for j in range(i+1, l):
				if S[i]+S[j] not in d:
					d[S[i]+S[j]] = [(i,j)]
				else:
					d[S[i]+S[j]].append((i,j))

		i = 0
		j = 0
		for i in range(l):
			for j in range(i+1, l-2):
				T = n - (S[i] + S[j])
				if T in d:
					for k in d[T]:
						if k[0] > j:
							res.add((S[i], S[j], S[k[0]], S[k[1]]))

		return [list(i) for i in res]

test = Solution()
S = [-3, -2, -1, 0, 0, 1, 2, 3]
print test.a4Sum(S, 0)

