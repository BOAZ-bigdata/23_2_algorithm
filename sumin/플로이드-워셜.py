#백준 11403

import sys
input = sys.stdin.readline

N = int(input())
graph = []

for k in range(n):
	row = list(map(int, input().split()))
	graph.append(row)

#플로이드-워셜
def find(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
    return graph

result = find(graph, N)

for i in range(N):
	for j in range(N):
		print(result[i][j], end=' ')
	print()

