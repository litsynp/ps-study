# p.298 그래프 이론 - 팀 결성
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
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


N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for i in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        # '팀 합치기' 연산
        union_parent(parent, a, b)
    else:
        # '같은 팀 여부 확인' 연산
        is_in_same_team = find_parent(parent, a) == find_parent(parent, b)
        print('Yes' if is_in_same_team else 'No')
