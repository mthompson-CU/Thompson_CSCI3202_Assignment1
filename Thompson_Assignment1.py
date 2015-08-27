# Author: Matthew Thompson
# Date: August 25, 2015
# Programming Assignment 1

import sys
import IntQueue
import Stack

def main(argv):

	# TESTING QUEUE

	intQ = IntQueue.IntQueue()

	for x in range(0, 10):
		intQ.put(x)
		print "Put integer " + str(x) + " to queue"
		

	while not intQ.empty():
		rmvd = intQ.get() 
		print "Got integer " + str(rmvd) + " from queue" 

	# TESTING STACK

	stack = Stack.Stack()

	for x in range(0, 10):
		stack.push(x)
		print "Pushed integer " + str(x) + " to stack"
		
	while not stack.checkSize() == 0:
		popped = stack.pop() 
		print "Popped integer " + str(popped) + " from stack" 

	return

if __name__ == "__main__":
	main(sys.argv)