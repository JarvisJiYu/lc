#!/bin/python

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, x, y):
		"""
		:type x: List
		:type y: List
		:rtype:
		"""

		if x == None:
			return y
		if y == None:
			return x

		flag = 0
		tmp = 0
		res = ListNode(-1)
		cur = res
		cur_x = x
		cur_y = y
		while cur_x and cur_y:
			sum = cur_x.val + cur_y.val + flag
			tmp = sum%10
			flag = sum/10
			if cur_x.val + cur_y.val >= 10:
				flag = 1
			cur.next = ListNode(tmp)
			cur = cur.next
			cur_x = cur_x.next
			cur_y = cur_y.next

		if cur_x:
			while cur_x:
				sum = cur_x.val + flag
				tmp = sum%10
				flag = sum/10
				cur.next = ListNode(tmp)
				cur = cur.next
				cur_x = cur_x.next
		if cur_y:
			while cur_y:
				sum = cur_y.val + flag
				tmp = sum%10
				flag = sum/10
				cur.next = ListNode(tmp)
				cur = cur.next
				cur_y = cur_y.next
				
		if flag == 1:
			cur.next = ListNode(flag)
			

		return res.next

def printList(l):
	print "************"
	while l:
		print l.val
		l=l.next

x0 = ListNode(0)
x1 = ListNode(1)
x2 = ListNode(7)
x3 = ListNode(5)
x0.next = x1
x1.next = x2
x2.next = x3
y0 = ListNode(2)
y1 = ListNode(1)
y2 = ListNode(7)
y3 = ListNode(5)
y4 = ListNode(9)
y5 = ListNode(9)
y0.next = y1
y1.next = y2
y2.next = y3
y3.next = y4
y4.next = y5

test = Solution()
printList(x0)
printList(y0)

sum = test.addTwoNumbers(x0, y0)
printList(sum)
