#!/bin/python

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def convertSortedListToBinarySearchTree1(self, S):
		"""
		:type S: ListNode
		:rtype:
		"""

		if not S:
			return None
		if S.next == None:
			return TreeNode(S.val)

		tmp1 = S
		tmp2 = S.next
		i = 0
		while tmp1.next and tmp2.next:
			if i%2:
				tmp1 = tmp1.next
			tmp2 = tmp2.next
			i += 1
		print tmp1.next.val
		root = TreeNode(tmp1.next.val)

		root.right = self.convertSortedListToBinarySearchTree1(tmp1.next.next)
		tmp1.next = None
		root.left = self.convertSortedListToBinarySearchTree1(S)

		return root
	def convertSortedListToBinarySearchTree(self, S):
		self.end = S
		return self.convertSortedListToBinarySearchTree1(S)

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
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
i = ListNode(9)
j = ListNode(10)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j
root = test.convertSortedListToBinarySearchTree(a)

print test.binaryTreeLevelOrderTraversal(root)
print test.binaryTreePreorderTraversal(root)
print test.binaryTreeInorderTraversal(root)
