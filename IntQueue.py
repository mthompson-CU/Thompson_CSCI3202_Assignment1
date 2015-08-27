# Author: Matthew Thompson
# Date: August 25, 2015
# Programming Assignment 1
# Implements a Queue that only accepts integers

import Queue

class IntQueue(Queue.Queue):
	def __init__(self, maxSize=0):
		Queue.Queue.__init__(self, maxSize)

	def put(self, item, block=True, timeout=None):
		# Inspired by http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
		if(not isinstance(item, int)):
			raise ValueError("'item' must be an integer")
		else: 
			self._put(item)