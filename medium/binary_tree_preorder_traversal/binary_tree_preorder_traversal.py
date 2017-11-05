#!/bin/python

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def preorderTraversal(self, root, list):
		stack = []
		while root or stack:
#			if root:
#				list.append(root.val)
#				stack.append(root.right)
#				stack.append(root.left)
#			root = stack.pop()
			if root:
				list.append(root.val)
				stack.append(root)
				root = root.left
			else:
				stack.pop()
				root = root.right

	def preorderTraversal_re(self, root, list):
		if root:
			list.append(root.val)
			self.preorderTraversal_re(root.left, list)
			self.preorderTraversal_re(root.right, list)

	def binaryTreePreorderTraversal(self, root):
		list = []
		#self.preorderTraversal(root, list)
		self.preorderTraversal_re(root, list)
		return list
			

root = TreeNode(10)
a = TreeNode(3)
b = TreeNode(6)
c = TreeNode(7)
d = TreeNode(8)
e = TreeNode(9)
f = TreeNode(11)
g = TreeNode(12)
root.left = b
root.right = f
b.left = a
b.right = e
e.left = d
d. left = c
f.right = g

test = Solution()
print test.binaryTreePreorderTraversal(root)
