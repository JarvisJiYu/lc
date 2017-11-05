#!/bin/python

class Solution:
	def removeDuplicatesFromSortedArray(self, a):
		"""
		:type a: List(int)
		:rtype: int
		:rtype: List(int)
		"""
		l = len(a)
		res_l = l

		before = a[0]
		j = 1
		print l
		for i in range(1,l):
			print i, j
			if a[i] == before:
				res_l = res_l - 1
			else:
				a[j] = a[i]
				j = j + 1
				before = a[i]

		return res_l, a

test = Solution()
a = [1, 1, 2, 5, 5, 7, 10]
print test.removeDuplicatesFromSortedArray(a)
