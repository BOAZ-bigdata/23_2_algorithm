import sys
input = sys.stdin.readline
from queue import PriorityQueue

v, e = map(int, input().split())
k = int(input())
dist = [sys.maxsize] * (v+1)
visited = [False] * (v+1)
myList = [[] for _ in range(v+1)]
q = PriorityQueue()

for _ in range(e):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

q.put((0, k))
dist[k] = 0

while q.qsize() > 0:
    now = q.get()
    c_v = now[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if dist[next] > dist[c_v] + value:
            dist[next] = dist[c_v] + value
            q.put((dist[next], next))

for i in range(1, v+1):
    if visited[i]:
        print(dist[i])
    else:
        print("INF")