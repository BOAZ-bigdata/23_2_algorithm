


'''
의사 코드
1. 섬에 대한 그리드를 input으로 입력 받음 이때 계속 입력 받으니 while문으로
2. 방문된 섬은 다시 방문하지 않기 위해서 방문처리할 리스트 필요
3. 스택의 개념을 이용해서 재귀 함수 구성??

4. 계속해서 탐색을 진행하는 것이니 시작 지점 설정
5. 그 점의 인접한 곳을 전부 탐색
5.1 이때 인접한 곳이 방문했으면 탐색 안함


'''


import sys
sys.setrecursionlimit(10000)


def dfs(y,x):
    # 범위 벗어나는 경우 건너뛰기(그리드 범위 밖일때)
    if x < 0 or x >= w or y < 0 or y >= h:
        return False

    # 바다인경우 건너뛰기
    # if graph[x][y]==0:
    #     return False

    # 섬인경우 재귀
    if graph[y][x] == 1:
        #다음에 재귀를 통해서 무한을 방지하기 위해 방문처리
        graph[y][x] = 0
        
		# 상하좌우 탐색
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        
		# 대각선 탐색
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        
        return True
    return False


while True:
    w,h = map(int,input().split())

    if w == 0 & h ==0 :
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
    print(result)