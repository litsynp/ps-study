# p.339 DFS/BFS 기출문제 - 특정 거리의 도시 찾기
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

# N: 도시의 개수
# M: 도로의 개수
# K: 거리 정보 (일치시킬 최단 거리)
# X: 출발 도시의 번호
N, M, K, X = map(int, input().split())
graph = {}

for i in range(M):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []

    graph[a].append(b)

# 출발 노드 X로부터 해당 노드까지의 최단 거리 배열
distances = [INF] * (N + 1)
distances[X] = 0

# 방문 배열
visited = [False] * (N + 1)


def bfs(graph, start, visited, distances):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()

        if v in graph:
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

                    # 원래 값과 새로운 값 중 짧은 거리를 저장
                    distances[i] = distances[v] + 1


# 최단 거리 계산
bfs(graph, X, visited, distances)

# 최단 거리 배열 중 K와 일치하는 노드 번호만 저장
ans = [i for i in range(len(distances)) if distances[i] == K]

# 존재하지 않는다면 -1, 존재한다면 순서대로 출력
if not ans:
    print(-1)
else:
    for a in ans:
        print(a)
"""
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4

7 7 3 1
1 2
1 3
2 4
2 5
3 6
4 5
6 7
"""
