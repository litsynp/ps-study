import sys
input = sys.stdin.readline

# =========================
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, v, visited)


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False] * 9

dfs(graph, 1, visited)

# =========================
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False] * 9

bfs(graph, 1, visited)
