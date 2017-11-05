#!/bin/python

class Solution:
	def isValidNine(self, s):
		temp = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
		for i in range(0, 9):
			ok = 0
			if s[i] == ".":
				continue
			if not s[i].isdigit():
				return False
			for j in range(0, 9):
				if int(s[i]) == temp[j]:
					temp[j] = 0
					ok = 1
					break
			if not ok:
				return False
		return True

	def validSudoku(self, s):
		"""
		:type s: string
		:rtype: bool
		"""
		if len(s) != 9:
			return False

		for i in range(0, 9):
			row = s[i]
			col = [c[i] for c in s]
			if not self.isValidNine(row):
				return False
			if not self.isValidNine(col):
				return False
		for i in [0, 3, 6]:
			for j in [0, 3, 6]:
				block = [s[m][n] for m in [i, i+1, i+2] for n in [j, j+1, j+2]]
				if not self.isValidNine(block):
					return False

		return True
			
	def validSudoku2(self, s):
		row = [[False for i in range(9)] for j in range(9)]
		col = [[False for i in range(9)] for j in range(9)]
		block = [[False for i in range(9)] for j in range(9)]

		for i in range(9):
			for j in range(9):
				if s[i][j] != '.':
					if not s[i][j].isdigit():
						return False
					num = int(s[i][j]) - 1
					k = i/3*3 + j/3

					if row[i][num] or col[i][num] or block[k][num]:
						return False
					row[i][num] = col[i][num] = block[k][num] = True
		return True

	def validSudoku3(self, s):
		seen = []
		for i, row in enumerate(s):
			for j, c in enumerate(row):
				if c != '.':
					seen += [(c,j), (i, c), (i/3, j/3, c)]

		return len(seen) == len(set(seen))

#test = Solution()
#a = "123456..9"
#b = "........8"
#c = "........7"
#d = "........6"
#e = "........5"
#f = ".5......4"
#g = "........3"
#h = "........2"
#i = "........1"
#s = [a, b, c, d, e, f, g, h, i]
#print test.validSudoku(s)
#print test.validSudoku2(s)
#print test.validSudoku3(s)
