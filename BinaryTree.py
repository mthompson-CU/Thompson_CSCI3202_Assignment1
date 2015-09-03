# Author: Matthew Thompson
# Date: August 25, 2015
# Programming Assignment 1
# Implements a Binary Tree
# Inspired by http://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree-in-python

import Node
import Queue

class BinaryTree():
	def __init__(self):
		self.root = None

	def add(self, key, parentKey=None):
		if (not isinstance(self.root, Node.Node)):
			self.root = Node.Node(key)
			return
		else:
			parentNode = self.searchTree(parentKey)

			if (not isinstance(parentNode, Node.Node)):
				print 'Parent not found'
				return

			if (not isinstance(parentNode.left, Node.Node)):
				parentNode.left = Node.Node(key)
				parentNode.left.parent = parentNode
			elif (isinstance(parentNode.left, Node.Node) and not isinstance(parentNode.right, Node.Node)):
				parentNode.right = Node.Node(key)
				parentNode.right.parent = parentNode
			elif (isinstance(parentNode.left, Node.Node) and isinstance(parentNode.right, Node.Node)):
				print 'Parent has two children, node not added'

		return

	def delete(self, key):
		node = self.searchTree(key)

		if (not isinstance(node, Node.Node)):
			print 'Node not found'
			return

		if (isinstance(node.left, Node.Node) or isinstance(node.right, Node.Node)):
			print 'Node not deleted, has children'
			return

		if (node == self.root):
			self.root = None
			return

		parentNode = self.searchTree(node.parent.key)

		if (parentNode.left.key == key):
			parentNode.left = None
		elif (parentNode.right.key == key):
			parentNode.right = None

		return

	def printTree(self):
		nodeQueue = Queue.Queue()

		node = self.root
		while (isinstance(node, Node.Node)):
			nodeQueue.put(node.left)
			nodeQueue.put(node.right)
			print node.key
			node = nodeQueue.get()

		return

	def searchTree(self, key):
		nodeQueue = Queue.Queue()
		
		node = self.root
		while (isinstance(node, Node.Node)):
			if (node.key == key):
				return node
			else:
				nodeQueue.put(node.left)
				nodeQueue.put(node.right)
				node = nodeQueue.get()

		return None