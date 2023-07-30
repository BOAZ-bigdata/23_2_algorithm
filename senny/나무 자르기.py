import sys
input = sys.stdin.readline
N, M = map(int, input().split())
height = list(map(int, input().split()))
height.sort()
start, end = 1, max(height) #가장 짧은 나무 1, 나무의 최대값

while start <= end:
    result = 0 #벌목된 나무의 총합
    mid = int((start + end) / 2) #중앙값의 인덱스
    for i in height:
        if i > mid: #나무가 절단 길이보다 길다면
            result += i - mid # 나무 길이 - 중앙값이 더해진다
        else: #나무가 절단 길이보다 짧다면
            result += 0 #잘리지 않는다
    if result >= M: #잘린 나무의 총합이 M보다 크거나 같다면
        start = mid + 1 # 가장 짧은 나무 길이 키우기
    else: #잘린 나무의 총합이 M보다 작다면
        end = mid - 1 # 나무의 최대값 줄이기

print(end) # 나무의 최대값