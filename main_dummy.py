from dummy_graph import RandomGraph

def main():

    dummyGraph = RandomGraph(10, directed=False)
    dummyGraph.view_graph()
    data_dfs = dummyGraph.dfs()
    print(f"Resultado Busqueda por Profundidad: {data_dfs}")
    data_bfs = dummyGraph.bfs()
    print()
    print(f"Resultado Busqueda por Anchura: {data_bfs}")


if __name__ == '__main__':
    main()
