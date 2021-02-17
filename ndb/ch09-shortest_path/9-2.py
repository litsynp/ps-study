# p.259 최단 경로 - 미래 도시
"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
"""

import sys
input = sys.stdin.readline
INF = int(1e9)

# N: number of vertices
# M: number of edges
N, M = map(int, input().split())

# graph: adjacency matrix
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# Initialize graph
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for i in range(M):
    a, b = map(int, input().split())

    # The edges are bidirectional
    graph[a][b] = 1
    graph[b][a] = 1

# Get X and K where:
# X: destination node
# K: stopover node
X, K = map(int, input().split())

# Floyd-Warshall
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for row in graph:
    print(row)

if graph[1][K] + graph[K][X] >= INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])
