import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
dist = [sys.maxsize]*(n+1)

for i in range(m):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

dist[1] = 0

for _ in range(n-1):
    for start, end, time in edges:
        if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
            dist[end] = dist[start] + time
    
mCycle = False

for start, end, time in edges:
    if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
            mCycle = True

if not mCycle:
    for i in range(2, n+1):
        if dist[i] != sys.maxsize:
            print(dist[i])
        else:
            print(-1)
else:
    print(-1)