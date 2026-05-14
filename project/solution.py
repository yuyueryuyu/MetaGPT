def floyd_warshall(graph):
    # Number of vertices in the graph
    n = len(graph)
    # Initialize the distance matrix with the input graph
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    # Set the distance from each vertex to itself to 0
    for i in range(n):
        dist[i][i] = 0
    # Update the distance matrix using the Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist