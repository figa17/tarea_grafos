from dummy_graph import RandomGraph

def main():
    print('creating tree')

    dummyGraph = RandomGraph(10, directed=False)
    dummyGraph.view_graph()
    data_dfs = dummyGraph.dfs()
    print(data_dfs)
    data_bfs = dummyGraph.bfs()
    print(data_bfs)


if __name__ == '__main__':
    main()
