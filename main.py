from dummy_graph import RandomGraph

def main():

    graph = RandomGraph(10, directed=False)
    graph.view_graph()
    data_dfs = graph.dfs()
    print(f"Resultado Busqueda por Profundidad: {data_dfs}")
    data_bfs = graph.bfs()
    print()
    print(f"Resultado Busqueda por Anchura: {data_bfs}")


if __name__ == '__main__':
    main()
