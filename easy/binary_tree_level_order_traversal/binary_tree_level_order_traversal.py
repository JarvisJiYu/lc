#!/usr/bin/python2.6

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def binaryTreeLevelOrderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		res = []
		if root == None:
			return res

		q = [root]
		while len(q) != 0:
			res.append([node.val for node in q])
			new_q = []
			for node in q:
				if node.left:
					new_q.append(node.left)
				if node.right:
					new_q.append(node.right)
			q = new_q

		return res

	def binaryTreeLevelOrderTraversal_dfs(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		res = []
		self.dfs(root, 0, res)
		return res

	def dfs(self, root, depth, res):
		if root == None:
			return res
		if len(res) < depth+1:
			res.append([])
		res[depth].append(root.val)
		self.dfs(root.left, depth+1, res)
		self.dfs(root.right, depth+1, res)

a = TreeNode(15)
b = TreeNode(7)
c = TreeNode(20)
d = TreeNode(9)
e = TreeNode(3)
e.left = d
e.right = c
c.left = a
c.right = b

test = Solution()

print test.binaryTreeLevelOrderTraversal(e)

print test.binaryTreeLevelOrderTraversal_dfs(e)
