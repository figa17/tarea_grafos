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

        # Paso 1: Agregar Raiz
        path.append(start)
        visited.add(start)
        if len(path) == len(self.graph.nodes):
            return path
        # Paso 2: Recorrer cada arista adyacente y agregar nodo no visitado
        for neighbour in self.graph.adj.get(start):
            if neighbour not in visited:
                # Paso 3: Realizar recorrido con nodo adyacente
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        return None



    def bfs(self, start= 0, target = None):
        # Paso 1: Agregar Raiz
        path = [start]
        nextlevel = [start]
        # Paso 2: Recorrer todos los nodos del siguiente nivel
        while nextlevel:
            thislevel = nextlevel
            nextlevel = []
            for v in thislevel:
                for w in self.graph.adj.get(v):
                    if w not in path:
                        path.append(w)
                        # Paso 3: Cambiar de nivel
                        nextlevel.append(w)
                if len(path) == len(self.graph.nodes):
                    return path
        return path