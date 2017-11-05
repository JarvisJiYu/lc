#!/bin/python

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def __init__(self, root):
		self.stack = []
		while root:
			self.stack.append(root)
			root = root.left

	def hasNext(self):
		if self.stack:
			return True
		return False

	def next(self):
		if not self.hasNext():
			return None
		res = self.stack.pop()
		tmp = res.right
		while tmp:
			self.stack.append(tmp)
			tmp = tmp.left

		return res


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

test = Solution(root)

while test.hasNext():
	next = test.next()
	print next.val
