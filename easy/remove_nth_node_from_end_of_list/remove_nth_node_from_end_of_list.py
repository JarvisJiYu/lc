#!/bin/python

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def removeNthNodeFromEndOfList(self, a, n):
		"""
		:type a: list
		:type n: int
		:rtype: list
		"""

		head = ListNode(0)
		head.next = a
		tmp1 = head
		tmp2 = head
		r = head
		for i in range(n):
			tmp1 = tmp1.next

		while tmp1:
			r = tmp2
			tmp1 = tmp1.next
			tmp2 = tmp2.next

		r.next = tmp2.next

		return head.next

def printList(a):
	while (a):
		print a.val
		a = a.next

#head = ListNode(0)
#a = ListNode(1)
#b = ListNode(2)
#c = ListNode(3)
#d = ListNode(4)
#e = ListNode(5)
#f = ListNode(6)
#g = ListNode(7)
#
#a.next = b
#b.next = c
#c.next = d
#d.next = e
#e.next = f
#f.next = g
#
#printList(a)
#test = Solution()
#printList(test.removeNthNodeFromEndOfList(a, 1))
##printList(test.removeNthNodeFromEndOfList(a, 2))
##printList(test.removeNthNodeFromEndOfList(a, 3))
##printList(test.removeNthNodeFromEndOfList(a, 4))
##printList(test.removeNthNodeFromEndOfList(a, 5))
##printList(test.removeNthNodeFromEndOfList(a, 6))
##printList(test.removeNthNodeFromEndOfList(a, 7))
