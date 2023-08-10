# 백준 1929
# M 이상 N 이하의 소수를 모두 출력 : 1줄에 1개씩
import math
import sys
input = sys.stdin.readline
M, N = map(int, input().split())

# 1차원 리스트 생성 : 0으로 초기화
number = [0] * (N+1)
for i in range(2, N+1, 1): # 리스트 값을 인덱스로 초기화
    number[i] = i

# 배수 삭제
for i in range(2, int(math.sqrt(N))+1): # 기준 포인터는 제곱근까지만 이동
    if number[i] == 0: # 0이면 연산 미수행
        continue
    for j in range(i+i, N+1, i): #1씩 증가시키면서 배수인지 판단하게 하면 시간초과 발생
        number[j] = 0 #0으로 변경

for i in range(M, N+1): # M부터 N까지
    if number[i] != 0: # 소수이면
        print(number[i]) #출력하기