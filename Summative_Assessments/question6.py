def minimum_spanning_tree(n):
    # Initialize the graph with n nodes and m edges
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                graph[i][j] = 1
                graph[j][i] = 1
    # Compute the sum of the lengths of all edges
    mst_value = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                mst_value += graph[i][j]
    return mst_value

print(minimum_spanning_tree(10))