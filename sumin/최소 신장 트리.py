#백준 1414

import sys
input = sys.stdin.readline

n = int(input())
graph = []

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

def kruskal(edges, n):
    parent = [i for i in range(n)]
    edges.sort(key=lambda x: x[2])  # 간선을 가중치 순으로 정렬
    min_spanning_tree = []
    total_weight = 0

    for edge in edges:
        a, b, weight = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            min_spanning_tree.append(edge)
            total_weight += weight

    return min_spanning_tree, total_weight

for _ in range(n):
    line = input().split()
    for i in range(n):
        if line[i] != '0':
            length = ord(line[i]) - ord('a') + 1 if 'a' <= line[i] <= 'z' else ord(line[i]) - ord('A') + 27 #ord 유니코드 반환
            graph.append((_, i, length))

min_spanning_tree, result_weight = kruskal(graph, n)
print(result_weight)
