#백준 1446

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
dp = [i for i in range(D+1)]

#다익스트라
for _ in range(N):
    start, end, length = map(int, input().split())
    if end - start >= length:
        dp[end] = min(dp[end], dp[start] + length)  # 최소 거리 갱신

print(dp[D])