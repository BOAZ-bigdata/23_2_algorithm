from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miros = []
visited = [False] * (N+1)

dx = [-1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    miro = list(input())
    if len(miro) == M:
        miros.append(miro)

def BFS(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and miros[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = True

BFS((0,0))

