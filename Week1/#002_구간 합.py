#002
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = [0]*(n+1)
array[1:] = list(map(int, input().split()))
D = [0]*(n+1)
value = 0

for i in range(1, n+1):
    value += array[i]
    D[i] = value

for _ in range(m):
    i, j = map(int, input().split())
    print(D[j]-D[i-1])