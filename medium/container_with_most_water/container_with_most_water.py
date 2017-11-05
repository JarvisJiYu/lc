#!/bin/python

class jpoint(object):
	def __init__(self, x, a1, a2):
		self.con = x
		self.mx = a1
		self.my = a2

class Solution:
	def containerWithMostWater(self, X):
		"""
		:type X: List[int]
		:rtype: int, int
		"""
		maxm = 0
		i = 0
		j = len(X) -1
		start = 0
		end = 0
		while i < j:
			if X[i] < X[j]:
				curm = X[i] * (j - i)
				if curm > maxm:
					maxm = curm
					start = i
					end = j
				i += 1
			else:
				curm = X[j] * (j - i)
				if curm > maxm:
					maxm = curm
					start = i
					end = j
				j -= 1

		return start, end
	def containerWithMostWater_fool(self, X):
		"""
		:type X: List[int]
		:rtype: int, int
		"""
		max_con = []
		for i in range(len(X)):
			max_cur_con = jpoint(0, 0, 0)
			for j in range(i+1, len(X)):
				cur_con = min(X[i], X[j]) * (j - i)
				if cur_con > max_cur_con.con:
					max_cur_con = jpoint(cur_con, i, j)

			max_con += [max_cur_con]

		max_res = jpoint(0, 0, 0)
		for i in range(len(max_con)):
			if max_con[i].con > max_res.con:
				max_res = max_con[i]
		return max_res.mx, max_res.my

X = [1, 3, 4, 5, 7, 3, 10, 2, 1]

test = Solution()
print test.containerWithMostWater(X)
print test.containerWithMostWater_fool(X)
