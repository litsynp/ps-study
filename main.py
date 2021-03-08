import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]

for a in range(1, V + 1):
    for b in range(1, V + 1):
        if a == b:
            graph[a][b] = 0

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, V + 1):
    for b in range(1, V + 1):
        print(graph[a][b] if graph[a][b] != INF else 'INFINITY', end=' ')
    print()