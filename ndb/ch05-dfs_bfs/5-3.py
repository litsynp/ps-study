import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))


def dfs(x, y):
    global graph, dx, dy

    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

    return False


ans = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            ans += 1

print(ans)

for row in graph:
    print(row)

"""
Test cases
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
