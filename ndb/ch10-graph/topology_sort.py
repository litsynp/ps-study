"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
from collections import deque
import sys
input = sys.stdin.readline

# V: number of vertices
# E: number of edges
V, E = map(int, input().split())
indegree = [0] * (V + 1)

# graph: adjacency list
graph = [[] for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)  # A -> B
    indegree[b] += 1  # indegree to node b is increased by 1


def topology_sort():
    result = []
    q = deque()

    # Insert nodes with indegree 0 for starters
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # Decrease indegree by 1 of each node
        # that is connected to the node now
        for i in graph[now]:
            indegree[i] -= 1  # Remove the incoming edge
            # Insert new nodes with indegree 0
            if indegree[i] == 0:
                q.append(i)

    return result


ans = topology_sort()

for i in ans:
    print(i, end=' ')
