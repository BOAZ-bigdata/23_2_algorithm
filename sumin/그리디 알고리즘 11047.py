import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []

for i in range(N):
    A[i].append(int(input()))

for i in range(N, -1):
    if K >= A[i]:
        N += K / A[i]
        K = K % A[i]

print(N)