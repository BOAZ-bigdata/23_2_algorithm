#백준 11657

import sys
input = sys.stdin.readline

INF = int(1e9) #무한 설정

#벨만포드
def bellman_ford(n, m, edges):
    distance = [INF] * (n + 1)
    distance[1] = 0

    for _ in range(n - 1):
        for a, b, c in edges:
            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c

    for a, b, c in edges:
        if distance[a] != INF and distance[b] > distance[a] + c:
            return [-1]

    return distance[2:]

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

result = bellman_ford(n, m, edges)
for distance in result:
    print(distance if distance != INF else -1)

