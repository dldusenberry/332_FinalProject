# Demi Dusenberry
# CS 332 Algorithms
# Final Project

import BFS
import DFS


if __name__ == '__main__':

# # BFS Driver code

# 	# Create a graph
# 	g = BFS.BFS()
# 	g.add_edge(0, 1)
# 	g.add_edge(0, 2)
# 	g.add_edge(1, 2)
# 	g.add_edge(2, 0)
# 	g.add_edge(2, 3)
# 	g.add_edge(3, 3)

# 	print("BFS traversal starting from vertex 2: ")
# 	g.bfs(2)


# DFS driver code

	# Create a graph
	g = DFS.DFS(); # Total 5 vertices in graph 
	g.add_edge(1, 0); 
	g.add_edge(0, 2); 
	g.add_edge(2, 1); 
	g.add_edge(0, 3); 
	g.add_edge(1, 4); 

	print("DFS traversal in order of node visited: ") 
	g.dfs()