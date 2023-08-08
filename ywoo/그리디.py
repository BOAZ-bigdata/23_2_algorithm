'''
의사코드

1. 회의 개수와 시작,끝을 입력으로 받음
2. 제일 먼저 시작시간이 빠른걸로 생각을 했으나 책에서는 가장 최적은 많은 회의를 배정하는 것이니 제일 빨리 끝나는 걸로 먼저 고름
3. 따라서 제일 빨리 끝나는 순으로 정렬하고 고름


'''










N = int(input())
A = [[0] * 2 for _ in range(N)]
for i in range(N):
    S, E = map(int, input().split())
    A[i][0] = E  # 종료시간 우선 정렬이 우선이기 때문에 0번째에 종료시간을 먼저 저장.
    A[i][1] = S



A.sort()
count = 0
end = -1


for i in range(N):
    if A[i][1] >= end:  # 겹치지 않는 다음 회의가 나온 경우
        end = A[i][0]  # 종료 시간 업데이트
        count += 1
print(count)