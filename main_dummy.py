from dummy_graph import RandomGraph

def main():
    print('creating tree')

    dummyGraph = RandomGraph(10, directed=False)
    dummyGraph.view_graph()
    data_plain_dfs = dummyGraph.dfs()
    print(data_plain_dfs)
    data_plain_bfs = dummyGraph.bfs()
    print(data_plain_bfs)


if __name__ == '__main__':
    main()
