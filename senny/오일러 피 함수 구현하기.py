# 백준 11689 : 사실 잘 이해 못했음...
# 1 ~ N의 범위에서 N과 서로소인 자연수의 개수
import sys
import math
input = sys.stdin.readline
N = int(input())
result = N

for i in range(2, int(math.sqrt(N)+1)): # 2 ~ 제곱근
    if N % i == 0: # i가 소인수
        result = result - (result / i) # 나눈 값을 빼준다
        while N % i == 0: #소인수가 될 때까지
            N /= i

if N > 1: # 누락되는 소인수 처리
    result -= result / N

print(int(result))