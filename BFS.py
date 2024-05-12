# Demi Dusenberry
# CS 332 Algorithms
# Final Project

import Queue
import Graph

class BFS(Graph.Graph):
	def __init__(self):
		super().__init__()
		self.color = "white"
		self.distance = 0
		self.previous = None
	
	def bfs(self, start):
		for vertex in self:
			vertex.color = "white"
			vertex.distance = 0
			vertex.previous = None
	
		start_vertex = self.get_vertex(start_vertex)
		start_vertex.distance = 0
		start_vertex.previous = None
		vert_queue = Queue.Queue()
		vert_queue.enqueue(start_vertex)
		while vert_queue.size() > 0:
			current = vert_queue.dequeue()
			print(current, end=" ")
			for neighbor in current.get_neighbors():
				if neighbor.color == "white":
					neighbor.color = "gray"
					neighbor.distance = current.distance + 1
					neighbor.previous = current
					vert_queue.enqueue(neighbor)
			current.color = "black"
