#!/bin/python

class Solution:
	def countAndSay(self, n):
		res = "1"
		i = 1
		for i in range(0, n-1):
			l = len(res)
			j = 1
			res_new =""
			tmp = res[0]
			count = 1
			while j < l:
				if res[j] == tmp:
					count += 1
				else:
					res_new += str(count) + tmp
					tmp = res[j]
					count = 1
				j += 1
			res_new += str(count) + tmp
			res = res_new

		return res
	def countAndSay2(self, n):
		res = "1"
		i = 1
		while i < n:
			l = len(res)
			j = 0
			res_new =""
			while j < l:
				if res[j] == '1':
					if j < l-1 and res[j+1] == '1':
						res_new += "21"
						j += 2
					else:
						res_new += "11"
						j += 1
				elif res[j] == '2':
					res_new += "12"
					j += 1
			res = res_new
			i+=1

		return res


#test = Solution()
#print test.countAndSay(1)
#print test.countAndSay(2)
#print test.countAndSay(3)
#print test.countAndSay(4)
#print test.countAndSay(5)
#print test.countAndSay(6)
#print test.countAndSay(7)
#print "xxxxxxxxxxxxxxxxxxxxxx"
#print test.countAndSay2(1)
#print test.countAndSay2(2)
#print test.countAndSay2(3)
#print test.countAndSay2(4)
#print test.countAndSay2(5)
#print test.countAndSay2(6)
#print test.countAndSay2(7)
