# Author: Matthew Thompson
# Date: August 25, 2015
# Programming Assignment 1
# Implements a Stack that only accepts integers
# Inspired by https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
# Checked implementation against http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html

class Stack():
	def __init__(self):
		self.list = [];

	def push(self, item):
		# Inspired by http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
		if(not isinstance(item, int)):
			raise TypeError("'item' must be an integer")
		else: 
			self.list.append(item)

	def pop(self):
		return self.list.pop()

	def checkSize(self):
		return len(self.list)
