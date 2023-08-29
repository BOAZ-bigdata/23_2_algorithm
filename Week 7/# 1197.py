import sys
from queue import PriorityQueue

input = sys.stdin.readline
v, e = map(int, input().split())
pq = PriorityQueue()
parent = [0]*(v+1)

for i in range(v+1):
    parent[i] = i

for i in range(e):
    start, end, w = map(int, input().split())
    pq.put((w, start, end))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < v-1:
    w, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += w
        useEdge += 1

print(result)