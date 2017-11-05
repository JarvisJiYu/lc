#!/bin/python

class Solution:
	def majorityElement(self, nums):
		"""
		:type nums: int array
		:rtype: string array
		"""
		major = 0
		count = 0
		for i in nums:
			if count == 0:
				major = i
				count = 1
			else:
				if major == i:
					count += 1
				else:
					count += -1

		return major


#test = Solution()
#nums = [12, 12, 13, 12, 14, 12, 133]
#print test.majorityElement(nums)
