# p.304 그래프 이론 - 커리큘럼
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

4
30 -1
20 -1
30 4 -1
40 1 2 -1
"""
from collections import deque
import copy
import sys
input = sys.stdin.readline

V = int(input())

# 강의별로 선수과목을 담은 그래프
graph = [[] for _ in range(V + 1)]

# 각 강의의 이수 시간을 담은 그래프
times = [0] * (V + 1)

# 진입차수 리스트
indegree = [0] * (V + 1)

# 각 강의별 필요한 시간
ans = [0] * (V + 1)

for b in range(1, V + 1):
    s = list(map(int, input().split()))
    times[b] = s[0]

    for a in s[1:-1]:
        graph[a].append(b)
        indegree[b] += 1


def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result


# 위상정렬을 이용해 강의별 수강까지 필요한 시간 계산
ans = topology_sort()

for i in range(1, V + 1):
    print(ans[i])
