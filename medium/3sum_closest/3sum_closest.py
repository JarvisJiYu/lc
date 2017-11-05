#!/bin/python

class Solution:
	def a3SumClosest(self, S, n):
		"""
		:type S: List(int)
		:type n: int
		:rtype: int
		"""
		min_sum = S[0] + S[1] + S[2]
		cur_sum = 0
		for i in range(0, len(S)-2):
			for j in range(i+1, len(S) -1):
				for k in range(j+1, len(S)):
					cur_sum = S[i] + S[j] + S[k]
					if abs(cur_sum - n) < abs(min_sum -n):
						min_sum = cur_sum
		return min_sum

	def a3SumClosest2(self, S, n):
		"""
		:type S: List(int)
		:type n: int
		:rtype: int
		"""
		S.sort()
		res = S[0] + S[1] + S[-1]
		for i in range(0, len(S) -2):
			tmp = n - S[i]
			j = i + 1
			k = len(S) - 1
			while j < k:
				if S[j] + S[k] == tmp:
					return target
				elif S[j] + S[k] > tmp:
					if S[j] + S[j+1] >= tmp:
						if S[j] + S[j+1] - tmp < abs(res - n):
							res = S[i] + S[j] + S[j+1]
						break;
					tmp_res = S[i] + S[j] + S[k]
					if tmp_res - target < abs(res - n):
						res = tmp_res
					k -= 1
				else:
					if S[k] + S[k-1] <= tmp:
						if tmp - S[k] - S[k-1] < abs(res - n):
							res = S[i] + S[k-1] + S[k]
						break;
					tmp_res = S[i] + S[j] + S[k]
					if target - tmp_res < abs(res - n):
						res = tmp_res
					j += 1

			if res == n:
				return target
		return res

test = Solution()
S = [-1, 2, 1, -4]
n = 1
print test.a3SumClosest(S, n)
print test.a3SumClosest2(S, n)
