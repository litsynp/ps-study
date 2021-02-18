# p.300 그래프 이론 - 도시 분할 계획
"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)
edges = []
ans = 0

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

# max_cost_mst: 'MST에 포함되는' 간선 중 최대 유지 비용을 갖는 간선의 비용
max_cost_mst = 0

# MST 구성
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost

        # 'MST에 포함되는' 간선 중 최대 유지 비용을 갖는 간선을 찾음
        max_cost_mst = cost

# 두 개의 MST로 분리
ans -= max_cost_mst
print(ans)
