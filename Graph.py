# Demi Dusenberry
# CS 332 Algorithms
# Final Project

import Vertex

# Maps vertex names to vertex objects
class Graph(Vertex.Vertex):
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        # Add a vertex
        self.vertices[key] = Vertex.Vertex(key)

    def get_vertex(self, key):
        # Returns vertex
        return self.vertices.get(key) 

    def __contains__(self, key):
        # Returns T/F
        return key in self.vertices

    def add_edge(self, from_vert, to_vert): 
        # Add an edge between 2 vertices 
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert]) 

    def get_vertices(self):
        # Returns the names of all the vertices in the graph
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
    