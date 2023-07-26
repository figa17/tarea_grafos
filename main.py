from graph import Graph
from distance import create_distance_matrix
import pandas as pd


def main():
    print('creating tree')

    data = pd.read_csv('data/data.csv', sep=';')

    distance_matrix = create_distance_matrix(data)

    n_nodes = len(distance_matrix)
    graph = Graph(n_nodes)
    for index, row in distance_matrix.iterrows():
        for i in range(n_nodes):
            if i != index and row[i] < 16:
                graph.add_edge(index, i, row[i])

    graph.print_adj_list()
    print(graph.bfs(0, 15))
    print(graph.dfs(0, 15))


if __name__ == '__main__':
    main()
