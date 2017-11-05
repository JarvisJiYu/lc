#!/bin/python

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def inorderTraversal(self, root, list):
		stack = []
		while root or stack:
			if root:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				list.append(root.val)
				root = root.right

	def inorderTraversal_re(self, root, list):
		if root:
			self.inorderTraversal_re(root.left, list)
			list.append(root.val)
			self.inorderTraversal_re(root.right, list)

	def binaryTreeInorderTraversal(self, root):
		list = []
		self.inorderTraversal(root, list)
		#self.inorderTraversal_re(root, list)
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
print test.binaryTreeInorderTraversal(root)
