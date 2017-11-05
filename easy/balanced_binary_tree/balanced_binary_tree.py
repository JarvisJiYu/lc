#!/bin/python

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def Height(self, root):
		if root == None:
			return 0
		return max(self.Height(root.left), self.Height(root.right)) + 1

	def isBalanced(self, root):
		if root == None:
			return True
		if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
			return self.isBalanced(root.left) and self.isBalanced(root.right)
		else:
			return False

a = TreeNode(15)
b = TreeNode(7)
c = TreeNode(20)
d = TreeNode(9)
e = TreeNode(3)
e.left = d
e.right = c
c.left = a
c.right = b

#f = TreeNode(100)
#f.left = e

test = Solution()

print test.isBalanced(e)
