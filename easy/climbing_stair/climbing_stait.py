#!/bin/python

class Solution:
	def climbingStair(self, n):
		if n == 0:
			return 0
		dp = [1 for i in range(n+1)]
		for i in range(2, n+1):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[n]

	def climbingStair_re(self, n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2

		return self.climbingStair_re(n-1) + self.climbingStair_re(n-2)

test = Solution()
print test.climbingStair(10)
print test.climbingStair(11)
print test.climbingStair(12)
print test.climbingStair_re(12)
print test.climbingStair(0)
print test.climbingStair(1)
print test.climbingStair(2)
print test.climbingStair(3)
print test.climbingStair(4)
print test.climbingStair_re(0)
print test.climbingStair_re(1)
print test.climbingStair_re(2)
print test.climbingStair_re(3)
print test.climbingStair_re(4)
