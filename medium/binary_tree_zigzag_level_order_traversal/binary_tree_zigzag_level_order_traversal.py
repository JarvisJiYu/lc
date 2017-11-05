#!/bin/python
import Queue

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def zigzagLevelOrderTraversal(self, root, list):
		if root == None:
			return 0
		stack = [root]
		level = 1
		while len(stack) != 0:
			list.append([node.val for node in stack])
			new_q = []
			while stack:
				node = stack.pop()
				if level%2 == 0:
					if node.left:
						new_q.append(node.left)
					if node.right:
						new_q.append(node.right)
				else:
					if node.right:
						new_q.append(node.right)
					if node.left:
						new_q.append(node.left)
			stack = new_q
			level += 1

	def zigzagLevelOrderTraversal_re(self, root, depth, res):
		if root == None:
			return res
		if len(res) < depth+1:
			res.append([])
		if depth%2 == 0:
			res[depth].append(root.val)
		else:
			res[depth].insert(0, root.val)
		self.zigzagLevelOrderTraversal_re(root.left, depth+1, res)
		self.zigzagLevelOrderTraversal_re(root.right, depth+1, res)

	def zigzagLevelOrderTraversal_queue(self, root, res):
		if root == None:
			return
		my_queue = Queue.Queue()
		my_queue.put(root)
		flag = True
		while not my_queue.empty():
			tmp = []
			size = my_queue.qsize()
			for i in range(size):
				node = my_queue.get()
				if node.left:
					my_queue.put(node.left)
				if node.right:
					my_queue.put(node.right)
				if flag:
					tmp.append(node.val)
				else:
					tmp.insert(0, node.val)

			res.append(tmp)
			flag = not flag


	def binaryTreeZigzagLevelOrderTraversal(self, root):
		list1 = []
		list2 = []
		list3 = []
		self.zigzagLevelOrderTraversal(root, list1)
		self.zigzagLevelOrderTraversal_re(root, 0,  list2)
		self.zigzagLevelOrderTraversal_queue(root, list3)
		return list1, list2, list3
			

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
print test.binaryTreeZigzagLevelOrderTraversal(root)
