from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import erdos_renyi_graph
import random


class RandomGraph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True, seed = random.seed(246)):
        self.graph = erdos_renyi_graph(num_of_nodes, p = 0.5, directed = directed, seed = seed)
        
    def view_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def dfs(self, start=0, target=None, path=None, visited=None):

        if visited is None:
            visited = set()
        if target is None:
            target = len(self.graph.nodes)- 1 
        if path is None:
            path = []

        path.append(start)
        visited.add(start)
        if len(path) == len(self.graph.nodes):
            return path
        for neighbour in self.graph.adj.get(start):
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        # path.pop()
        return None



    def bfs(self, start= 0, target = None):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()
        
        if target is None:
            target = len(self.graph.nodes)- 1 

        # Add the start to the queue and visited list

        queue.put(start)
        visited.add(start)

        # start has not parents
        parent = dict()
        parent[start] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if len(parent) == 10:
                path_found = True
                break
            # if queue.qsize() == len(self.graph.nodes):
            #     path_found = True
            #     break

            for next_node in self.graph.adj.get(current_node):
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)

        # Path reconstruction
        print(f"parent: {parent}")
        path = []
        if path_found:
            path.append(target)
            while parent[target] is not None:
                path.append(parent[target])
                target = parent[target]
            path.reverse()
        return path