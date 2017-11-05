#!/bin/python

class Solution:
	def removeElement(self, a, x):
		"""
		:type a: List(int)
		:type x: int
		:rypte: int
		"""
		l = len(a)

		j = 0
		for i in range(0, l):
			if a[i] != x:
				a[j] = a[i]
				j = j + 1

		return j, a

#test = Solution()
#a = [1,2,3,4,5,6]
#b = [1,1,1,1,1,1]
#
#print test.removeElement(a, 3)
#print test.removeElement(b, 1)
