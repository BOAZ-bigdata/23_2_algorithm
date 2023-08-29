#백준 1197

import sys
input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def kruskal(edges, v):
    parent = [i for i in range(v + 1)]
    edges.sort(key=lambda x: x[2])  # 간선을 가중치 순으로 정렬
    total_weight = 0

    for edge in edges:
        a, b, weight = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            total_weight += weight

    return total_weight

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

answer = kruskal(edges, v)
print(answer)
