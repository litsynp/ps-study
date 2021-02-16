import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# V: number of vertices
# E: number of edges
V, E = map(int, input().split())

# graph: adjacency list
graph = [[] for i in range(V + 1)]

# start: starting node
start = int(input())

# distance: array that has distance from starting node to each node
distance = [INF] * (V + 1)

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    # Initialize min heap queue and distance array
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # Get current node from the queue
        dist, now = heapq.heappop(q)
        
        # Check if the distance has already been updated
        if distance[now] < dist:
            continue

        # Check every node that is connected to the current node
        for i in graph[now]:
            cost = dist + i[1]

            # Compare the new cost and the original cost
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V + 1):
    print(distance[i] if distance[i] != INF else 'INFINITY')
