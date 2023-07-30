# 백준 24060
# 병합 정렬

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = [] #정렬 결과

def merge_sort(arr):
    if len(arr) == 1: #데이터가 1개라면
        return arr
    
    mid = (len(arr) + 1) // 2 # 중앙 인덱스
    # 재귀 호출
    low = merge_sort(arr[:mid]) #앞쪽 데이터
    high = merge_sort(arr[mid:]) #뒤쪽 데이터
    
    new = []
    l = h = 0 #l과 h는 같이 움직인다
    while l < len(low) and h < len(high): #low 리스트 내 l과 high 리스트 내 h에 대해서
        if low[l] < high[h]: #low 리스트와 high 리스트 중에서
            new.append(low[l]) #큰 값을 new, answer에 append
            answer.append(low[l])
            l += 1 #큰 쪽의 인덱스를 1 증가시킴
        else:
            new.append(high[h])
            answer.append(high[h])
            h += 1
    while l < len(low): #low 리스트가 남아있다면 붙이기
        new.append(low[l])
        answer.append(low[l])
        l += 1
    while h < len(high): #high 리스트가 남아있다면 붙이기
        new.append(high[h])
        answer.append(high[h])
        h += 1
    
    return new

merge_sort(arr)

# 저장 횟수 : len(answer)
if len(answer) < K:
    print(-1) #저장 횟수가 k보다 작으면 -1 출력
else:
    print(answer[K-1]) #K번째 저장되는 수 출력