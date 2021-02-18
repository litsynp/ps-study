import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# V: number of vertices
# E: number of edges
V, E = map(int, input().split())

# Initialize parent table
parent = [0] * (V + 1)

# edges: edge list
# result: Total cost
edges = []
result = 0

# Initialize parent of each node as themselves
for i in range(1, V + 1):
    parent[i] = i

# Get edges information as input
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # Union only if adding the edge does not create a cycle
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
