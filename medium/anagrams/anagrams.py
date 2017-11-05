#!/bin/python

class Solution:
	def isPalindrome(self, s):
		if not S or len(s) == 0:
			return False
		new_s = s[::-1]
		if s == new_s:
			return True
		return False

	def palindromes(self, S):
		"""
		:type S: List[string]
		:rtype: List[string]
		"""
		res = []

		for s in S:
			if self.isAnagram(s):
				res.append(s)
		return res

	def anagrams(self, S):
		"""
		:type S: List[string]
		:rtype: List[string]
		"""
		d = {}
		res = []
		for s in S:
			k = ''.join(sorted(s))
			if k not in d:
				d[k] = [s]
			else:
				d[k].append(s)
		for T in d:
			if len(d[T]) >= 2:
				res += d[T]
		return res

test = Solution()
S = ["aaa", "abc", "acdfafdca", "acdfafcca", "bca"]
print test.anagrams(S)
