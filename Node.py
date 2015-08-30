# Author: Matthew Thompson
# Date: August 25, 2015
# Programming Assignment 1
# Implements a Node to be used in a Binary Tree
# Inspired by https://www.ics.uci.edu/~pattis/ICS-33/lectures/treesi.txt

class Node():
	def __init__(self, key, left=None, right=None, parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent


