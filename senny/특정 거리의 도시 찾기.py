# 백준 18352
# BFS

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

# 인접 리스트 초기화
A = [[] for _ in range(N+1)]
# 방문 기록 리스트 초기화
visit = [False] * (N+1)
## 0로 초기화하는 이유 : 최단 거리는 항상 0이라고 가정하기 때문
distance = [0] * (N+1)
# 거리가 K인 경우를 저장할 리스트
answer = []

for _ in range(M):
    s, e = map(int, input().split())
    # 인접 리스트 생성 : 단방향
    A[s].append(e)

def BFS(v):
    queue = deque()
    queue.append(v)
    visit[v] = True
    distance[v] = 0
    while queue:
        now = queue.popleft() # 현재 노드 삭제
        for i in A[now]:
            if not visit[i]: #방문하지 않았다면
                visit[i] = True
                queue.append(i)
                distance[i] = distance[now] + 1 # 현재 거리에 1 더하기
                if distance[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1) #거리가 k인 경우가 없다면 -1 출력
    else:
        answer.sort()
        for i in answer: #거리가 k인 경우 출력
            print(i, end = '\n')

BFS(X)