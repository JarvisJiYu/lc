#!/bin/python

class Solution:
	def a3Sum(self, S):
		"""
		:type S: List[int]
		:rtype: List[List[int]]
		"""

		l = len(S)
		S.sort()
		res = []

		for i in range(0, l):
			j = i+1
			k = l-1
			if i != 0 and S[i] == S[i-1]:
				continue

			while j < k:
				if S[i] + S[j] + S[k] == 0:
					res.append((S[i],S[j],S[k]))
					j += 1
					k -= 1
					while j < k and S[j] == S[j-1]:
						j+=1
					while j < k and S[k] == S[k-1]:
						k-=1

				if S[i] + S[j] + S[k] > 0:
					if S[i] + S[j] + S[j+1] > 0:
						print (S[i],S[j],S[k])
						break
					while j < k:
						k -= 1
						if S[k] < S[k+1]:
							break;
				else:
					if S[i] + S[k] + S[k-1] < 0:
						print (S[i],S[j],S[k])
						break
					while j < k:
						j += 1
						if S[j] > S[j-1]:
							break;

		return res

test = Solution()
S = [5, -3, -3, -3, -3,  -2, -2,  -1, 0, 1, 1, 1, 1, 2, 2, 2, 2]
print test.a3Sum(S)
