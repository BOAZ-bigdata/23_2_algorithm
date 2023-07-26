# 삽입 정렬 : 내림차순으로 정렬
# 백준 25305

# first try : shift 과정 오류로 틀림
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
score = list(map(int, input().split()))

for i in range(1, N): # 1~N만큼 반복
    point = i
    value = score[i]
    for j in range(i-1, -1, -1): #앞의 값과 비교
        if score[i] > score[j]: #앞의 값보다 크다면
            point = j-1 #삽입 위치 : 앞의 값보다 앞
        else: #앞의 값보다 작다면
            point = j+1 # 삽입 위치 : 앞의 값보다 뒤

    # 삽입을 위해 삽입 위치 ~ 현재의 값을 하나씩 밀기
    for j in range(i, point, -1):
        score[j] = score[j-1]
    score[point] = value
        
print(score[K-1])

# 해결 : for 대신 while로 해결
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
score = list(map(int, input().split()))

for i in range(1, N):
    value = score[i]
    j = i -1
    while j >= 0 and value > score[j]: #앞의 값보다 클 경우
        score[j+1] = score[j] #하나씩 뒤로 밀기
        j -= 1 #j 감소시키기
    score[j+1] = value #삽입하기

print(score[K-1])