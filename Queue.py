# Demi Dusenberry
# CS 332 Algorithms
# Final Project

# Queue implementation as a list
# Used for BFS
class Queue:

    def __init__(self):
        # Create new queue
        self._items = []

    def is_empty(self):
        # Check if the queue is empty
        return not bool(self._items)

    def enqueue(self, item):
        # Add an item to the queue
        self._items.insert(0, item)

    def dequeue(self):
        # Remove an item from the queue
        return self._items.pop()

    def size(self):
        # Get the number of items in the queue
        return len(self._items)