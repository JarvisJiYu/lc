#!/bin/python

class Solution:
	def compareVersionNumbers(self, version1, version2):
		"""
		:type version1: string
		:type version2: string
		:rtype : int
		"""
		res = 0
		num1 = version1.split('.')
		num2 = version2.split('.')
		while len(num1) or len(num2):
			if len(num1) == 0:
				return -1
			elif len(num2) == 0:
				return 1
			else:
				i1 = int(num1[0])
				i2 = int(num2[0])
				if i1 < i2:
					return -1
				elif i1 > i2:
					return 1
				else:
					num1 = num1[1:]
					num2 = num2[1:]
		return 0

test = Solution()
print test.compareVersionNumbers("1.1.1.1", "2.3.4")
print test.compareVersionNumbers("2.1.1.1", "2.3.4")
print test.compareVersionNumbers("2.3.4", "2.3.4")
print test.compareVersionNumbers("2.3.4.1", "2.3.4")
