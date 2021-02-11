from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# [0][0] to [N-1][M-1]
N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().strip())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            # 다음 방문하려는 좌표
            nx, ny = x + dx[i], y + dy[i]

            # 경계 충돌시 방문하지 않음
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 괴물 존재시 방문하지 않음
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 지점일 경우, 경로 수 최신화
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs(0, 0)
print(graph[N - 1][M - 1])

"""
Test cases
5 6
101010
111111
000001
111111
111111

10 10
1111011111
1000000011
1111111111
0000011011
0101010011
1111111111
0010000000
1111011111
1010010101
0011110111
"""
