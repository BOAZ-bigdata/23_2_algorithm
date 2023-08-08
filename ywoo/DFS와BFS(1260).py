

'''
의사 코드 

1. 먼저 입력 받은 노드들과 정점간의 연결을 구현한다
2. BFS는 시작노드에서 시작해서 큐를 이용해서 사용하니 큐를 선언하고 먼저 하나를 집어넣고 방문처리를 위해서 방문처리 리스트를 만들고 방문처리
3. 이후 계속 연결 된 것들을 탐색

'''





from collections import deque

N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]


for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)
for i in range(N + 1):
    A[i].sort()  # 번호가 작은 노드 부터 방문하기 위해 정렬하기
visited = [False] * (N + 1)

def BFS(v):
    queue = deque()
    #v를 큐에 넣기
    queue.append(v)
    #현재 v를 방문 처리
    visited[v] = True
    
    while queue:
		#큐에서 제일 아래에 있는 것을 추출해서 현재 노드라고 설정
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        
		#현재 노드와 연결된 노드들을 추출해서 
        for i in A[now_Node]:
            #방문하지 않았다면 
            if not visited[i]:
				#방문하고 큐에 현재 노드를 넣기
                visited[i] = True
                queue.append(i)


print()
BFS(Start)