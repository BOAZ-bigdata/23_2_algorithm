import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
M = int(input())
# 인접 리스트 초기화
A = [[] for _ in range(N+1)]
# 방문 기록 리스트 초기화
visit = [False] * (N+1)

def DFS(v):
    # 현재 방문한 곳 True로 변경
    visit[v] = True
    for i in A[v]: #연결 노드 중
        if not visit[i]: #방문하지 않은 노드에 대해
            DFS(i) #DFS 실행

for _ in range(M):
    s, e = map(int, input().split())
    # 인접 리스트 생성
    A[s].append(e)
    A[e].append(s)

DFS(1) #1에 대해서는 DFS 실행
print(sum(visit) -1) #방문한 노드 중 하나 제외(1 자기 자신)