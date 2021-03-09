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
        b = parent[a]
    else:
        a = parent[b]


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

for i in range(E):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, V + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 집합: ', end='')
for i in range(1, V + 1):
    print(parent[i], end=' ')
