#!/bin/python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def maximumDepthOfBinaryTree(self, tree):
		"""
		:type tree: tree
		:rtype: int
		"""
		if tree == None:
			return 0

		left_res = self.maximumDepthOfBinaryTree(tree.left)
		right_res = self.maximumDepthOfBinaryTree(tree.right)
		return max(left_res, right_res) + 1

#a = TreeNode(15)
#b = TreeNode(7)
#c = TreeNode(20)
#d = TreeNode(9)
#e = TreeNode(3)
#e.left = d
#e.right = c
#c.left = a
#c.right = b
#
#f = TreeNode(100)
#b.right = f
#
#test = Solution()
#print test.maximumDepthOfBinaryTree(a);
#print test.maximumDepthOfBinaryTree(b);
#print test.maximumDepthOfBinaryTree(c);
#print test.maximumDepthOfBinaryTree(d);
#print test.maximumDepthOfBinaryTree(e);
#print test.maximumDepthOfBinaryTree(f);
