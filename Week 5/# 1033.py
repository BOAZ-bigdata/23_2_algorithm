n = int(input())
A = [[] for _ in range(n)]
visited = [False] * n
D = [0] * n
lcm = 1

def gcd(a, b): # 유클리드 호제법 이용 최대공약수 구현
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def DFS(v): # DFS 탐색 함수 구현
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v]*i[2] // i[1]
            DFS(next)

for i in range(n-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    lcm *= (p*q // gcd(p,q)) # 최소공배수는 두 수의 곱을 최대공약수로 나눈 것

D[0] = lcm
DFS(0)
mgcd = D[0]

for i in range(1, n):
    mgcd = gcd(mgcd, D[i])

for i in range(n):
    print(int(D[i] // mgcd), end=' ')