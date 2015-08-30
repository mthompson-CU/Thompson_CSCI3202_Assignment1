# Author: Matthew Thompson
# Identikey: math1906
# Date: August 25, 2015
# Programming Assignment 1

import sys
import IntQueue
import Stack
import BinaryTree
import Graph

def main(argv):

	# TESTING QUEUE

	print '\nTESTING QUEUE\n'

	intQ = IntQueue.IntQueue()

	for x in range(0, 10):
		intQ.put(x)
		print "Put integer " + str(x) + " to queue"
		
	while not intQ.empty():
		rmvd = intQ.get() 
		print "Got integer " + str(rmvd) + " from queue" 

	# TESTING STACK

	print '\nTESTING STACK\n'

	stack = Stack.Stack()

	for x in range(0, 10):
		stack.push(x)
		print "Pushed integer " + str(x) + " to stack"
		
	while not stack.checkSize() == 0:
		popped = stack.pop() 
		print "Popped integer " + str(popped) + " from stack" 

	# TESTING BINARY TREE

	print '\nTESTING BINARY TREE\n'

	binTree = BinaryTree.BinaryTree()

	binTree.add(0)

	# add two leaves at a time to fill each parent node
	beingAdded = 1
	for x in range(0, 5):
		binTree.add(beingAdded, x)
		print "Added integer " + str(beingAdded) + " to tree" 
		binTree.add(beingAdded+1, x)
		print "Added integer " + str(beingAdded+1) + " to tree" 
		beingAdded += 2

	binTree.printTree()

	for x in range(0, 5):
		binTree.delete(10 - x)
		print "Deleted integer " + str(10 - x) + " from tree"

	binTree.printTree()

	# TESTING GRAPH

	print '\nTESTING BINARY TREE\n'

	graph = Graph.Graph()

	for x in range(0, 10):
		graph.addVertex(x)	

	for x in range(0, 10):
		graph.addEdge(x, (x+1)%10)
		graph.addEdge(x, (x+2)%10)

	for x in range(0, 5):
		graph.findVertex(x)

	return

if __name__ == "__main__":
	main(sys.argv)