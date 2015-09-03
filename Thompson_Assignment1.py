# Author: Matthew Thompson
# IdentiKey: math1906
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

	print '\nTesting queue corner cases'

	print '\n-> Adding a non-integer value to queue\n'

	intQ.put('a')

	# TESTING STACK

	print '\nTESTING STACK\n'

	stack = Stack.Stack()

	for x in range(0, 10):
		stack.push(x)
		print "Pushed integer " + str(x) + " to stack"
		
	while not stack.checkSize() == 0:
		popped = stack.pop() 
		print "Popped integer " + str(popped) + " from stack" 

	print '\nTesting stack corner cases'

	print '\n-> Adding a non-integer value to stack\n'

	stack.push('a')

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

	print '\nTesting binary tree corner cases'

	print '\n-> Adding a node to a node with two children\n'

	binTree.add(12, 0)

	print '\n-> Adding a node to a node that is not in the tree\n'

	binTree.add(13, 12)

	print '\n-> Deleting a node that has children\n'

	binTree.delete(0)

	print '\n-> Deleting a node that is not in the tree\n'

	binTree.delete(15)

	# TESTING GRAPH

	print '\nTESTING GRAPH\n'

	graph = Graph.Graph()

	for x in range(0, 10):
		graph.addVertex(x)	

	for x in range(0, 10):
		graph.addEdge(x, (x+1)%10)
		graph.addEdge(x, (x+2)%10)

	for x in range(0, 5):
		graph.findVertex(x)

	print '\nTesting graph corner cases'

	print '\n-> Adding a vertex that is already in the graph\n'

	graph.addVertex(0)

	print '\n-> Adding an edge with a node that is not in the graph\n'

	graph.addEdge(0, 42)

	# ADDITIONAL CODE TO PRINT PICTURE OF GRAPH

	# import networkx as nx
	# import matplotlib.pyplot as plt

	# graph = nx.Graph()

	# for x in range(0, 10):
	# 	graph.add_node(x)

	# for x in range(0, 10):
	# 	graph.add_edge(x, (x+1)%10)
	# 	graph.add_edge(x, (x+2)%10)

	# nx.draw(graph)
	# plt.show()

	return

if __name__ == "__main__":
	main(sys.argv)