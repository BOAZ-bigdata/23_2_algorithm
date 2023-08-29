#백준 1738

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(m):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

#벨만포드
def belman_ford(graph, start, n):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0

    for i in range(n-1):
        for u,v,w in graph:
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] != INF and distance[u] + w < distance[v]:
            return None  #음수

    return distance

result = belman_ford(graph, 1, n)

if result is None:
    print(-1)
else:
    tmp = [n]
    current = n
    while current != 1:
        for u,v,w in graph:
            if result[current] == result[v]+w:
                tmp.append(v)
                current = v
                break
    tmp.reverse()
    print("".join(map(str, tmp)))
