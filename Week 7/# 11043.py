n = int(input())
dist = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    dist[i] = list(map(int, input().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] == 1 and dist[k][j] == 1:
                dist[i][j] = 1

for i in range(n):
    for j in range(n):
        print(dist[i][j], end=' ')
        print()