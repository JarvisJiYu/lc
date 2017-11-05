#!/usr/bin/python2.6


class Solution(object):
	def addBinary_invert(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		return bin(int(a, 2) + int(b, 2))[2:]

	def addBinary_bit(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		res = ''
		i, j, plus = len(a)-1, len(b)-1, 0
		while i>=0 or j>=0 or plus == 1:
#			plus += int(a[i]) if i>= 0 else 0
			if i>=0:
				plus+=int(a[i])
			else:
				plus+=0
			plus += int(b[j]) if j>= 0 else 0
			res = str(plus % 2) + res
			i, j, plus = i-1, j-1, plus/2
		return res

	def addBinary_bit_re(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		if not a or not b:
			return a if a else b
		if a[-1]=='1' and b[-1]=='1':
			return self.addBinary_bit_re(self.addBinary_bit_re(a[:-1], b[:-1]), '1') + '0'
		elif a[-1]=='0' and b[-1]=='0':
			return self.addBinary_bit_re(a[:-1], b[:-1]) + '0'
		else:
			return self.addBinary_bit_re(a[:-1], b[:-1]) + '1'

test = Solution()
print test.addBinary_invert("1111111111111111010100101010001001010100100100", "111001010101010101010110010101010101010010011001010101")
print test.addBinary_bit("1111111111111111010100101010001001010100100100", "111001010101010101010110010101010101010010011001010101")
print test.addBinary_bit_re("1111111111111111010100101010001001010100100100", "111001010101010101010110010101010101010010011001010101")
