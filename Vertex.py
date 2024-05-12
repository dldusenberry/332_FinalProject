# Demi Dusenberry
# CS 332 Algorithms
# Final Project

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {} 

    def get_neighbor(self, other):
        return self.neighbors.get(other) 

    def set_neighbor(self, other): 
        # Add a connection from this vertex to another
        self.neighbors[other] = other 

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return (
            str(self.key)
            + " connected to: "
            + str([x.key for x in self.neighbors])
        )

    def get_neighbors(self):
        # Returns all of the vertices in the adjacency list
        # as represented by the neighbors instance
        return self.neighbors.keys()

    def get_key(self):
        return self.key