#!/bin/python

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def constructBinaryTreeFromInorderAndPostorderTraversal(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: List[TreeNode]
		"""
		if len(inorder) == 0:
			return None
		if len(inorder) == 1:
			return TreeNode(inorder[0])
		root = TreeNode(postorder[-1])
		for i in range(0, len(inorder)):
			if inorder[i] == root.val:
				root.left = self.constructBinaryTreeFromInorderAndPostorderTraversal(inorder[:i], postorder[:i])
				root.right = self.constructBinaryTreeFromInorderAndPostorderTraversal(inorder[i+1:], postorder[i:-1])

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
		


inorder = [4, 2, 9, 8, 1, 3, 6, 5, 7]
postorder = [4, 9, 8, 2, 6, 7, 5, 3, 1]
test = Solution()
print inorder[:0]
print postorder[4:-1]
root = test.constructBinaryTreeFromInorderAndPostorderTraversal(inorder, postorder)
print test.binaryTreeLevelOrderTraversal(root)
print test.binaryTreePreorderTraversal(root)
