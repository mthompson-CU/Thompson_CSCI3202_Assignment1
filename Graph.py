# Author: Matthew Thompson
# IdentiKey: math1906
# Date: August 30, 2015
# Programming Assignment 1
# Implements a Graph
# Dictionary structure inspired by https://www.python.org/doc/essays/graphs/

class Graph():
	def __init__(self):
		self.vertices = {}

	def addVertex(self, vertex):
		if(not vertex in self.vertices):
			self.vertices[vertex] = []
			print 'Added vertex ' + str(vertex) + ' to graph'
		else:
			print 'Vertex already exists'
		return

	def addEdge(self, vertex1, vertex2):
		if (vertex1 in self.vertices and vertex2 in self.vertices):
			self.vertices[vertex1].append(vertex2)
			self.vertices[vertex2].append(vertex1)
			print 'Added edge from ' + str(vertex1) + ' to ' + str(vertex2)
		else:
			print 'One or more vertices not found'
		return

	def findVertex(self, vertex):
		if (vertex in self.vertices):
			print str(vertex) + ': ' + str(self.vertices[vertex])
		else:
			print 'Vertex not found'
		return
