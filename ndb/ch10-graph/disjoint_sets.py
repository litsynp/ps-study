import sys
input = sys.stdin.readline


# Find the set where a specific element belongs
def find_parent(parent, x):
    # If not root node, recursively call until it's the root
    # Also update parent table
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# Union two sets where two elements belong
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)

# Initialize parent of each node as themselves
for i in range(1, V + 1):
    parent[i] = i

# Union each node
for i in range(E):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# Print the set where each node belongs
print('각 원소가 속한 집합: ', end='')
for i in range(1, V + 1):
    print(find_parent(parent, i), end=' ')

print()

# Print parent table information
print('부모 테이블: ', end='')
for i in range(1, V + 1):
    print(parent[i], end=' ')
