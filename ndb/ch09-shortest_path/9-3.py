# p.262 최단 경로 - 전보
"""
3 2 1
1 2 4
1 3 2
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# N: number of vertices
# M: number of edges
# C: the city in emergency
N, M, C = map(int, input().split())

# graph: adjacency list
# distance: distance from city C to other cities
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)

contacts = list(filter(lambda d: d < INF, distance[1:]))
total_cities = len(contacts) - 1
total_time = max(contacts)

print(total_cities, total_time)
