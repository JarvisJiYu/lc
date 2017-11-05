#!/bin/python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def convertSortedArrayToBinarySearchTree(self, S):
		"""
		:type S: List[int]
		:rtype:
		"""

		if len(S) == 0:
			return None
		if len(S) == 1:
			return TreeNode(S[0])

		tmp = len(S)/2
		root = TreeNode(S[tmp])

		root.left = self.convertSortedArrayToBinarySearchTree(S[:tmp])
		root.right = self.convertSortedArrayToBinarySearchTree(S[tmp+1:])

		return root

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

	def inorderTraversal_re(self, root, list):
		if root:
			self.inorderTraversal_re(root.left, list)
			list.append(root.val)
			self.inorderTraversal_re(root.right, list)

	def binaryTreeInorderTraversal(self, root):
		list = []
		#self.inorderTraversal(root, list)
		self.inorderTraversal_re(root, list)
		return list

test = Solution()
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = test.convertSortedArrayToBinarySearchTree(S)

print test.binaryTreeLevelOrderTraversal(root)
print test.binaryTreePreorderTraversal(root)
print test.binaryTreeInorderTraversal(root)
