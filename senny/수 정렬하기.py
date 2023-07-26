# 백준 2750번
# 버블 정렬로 풀이
# 아래와 같이 풀이 시 교재 정답보다 시간 및 코드 길이 단축

import sys
input = sys.stdin.readline
N = int(input())
num = [int(input()) for _ in range(N)]

def swap(a, b): #swap 함수
    tmp = num[a]
    num[a] = num[b]
    num[b] = tmp

for i in range(N-1):
    for j in range(N-i-1): #범위 지정
        if num[j] > num[j+1]: #앞의 수가 더 크다면
            swap(j, j+1) #둘의 위치를 변경

for i in range(N):
    print(num[i])