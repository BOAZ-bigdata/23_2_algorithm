import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(v):
    visited[v] = True
    for i in A[v]: #재귀함수
        if not visited[i]:
            DFS(i)

for i in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

count = 0

for i in range(1, N+1):
    if not visited:
        count += 1
        DFS(i)

print(count)

