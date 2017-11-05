#!/bin/python

class Solution:
	def deleteNodeInALinkedList(self, node):
		"""
		:type node: ListNode
		:rtype: None
		"""
		if node == None or node.next == None:
			print "Wrong node"
			return
		node.val = node.next.val
		node.next = node.next.next

		return
#class ListNode(object):
#	def __init__(self, x):
#		self.val = x
#		self.next = None
#
#
#def printList(node):
#	while True:
#		print node.val
#		node = node.next
#		if node == None:
#			break
#	return	
#
#a = ListNode(1)
#b = ListNode(2)
#c = ListNode(3)
#d = ListNode(4)
#e = ListNode(5)
#
#a.next = b
#b.next = c
#c.next = d
#d.next = e
#
#printList(a)
#
#test = Solution()
#test.deleteNodeInALinkedList(c)
#
#printList(a)
