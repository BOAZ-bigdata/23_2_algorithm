# 백준 9613
import sys
input = sys.stdin.readline
t = int(input())

# A와 B의 최대공약수 출력하기
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) # 재귀 형태

for _ in range(t):
    number = list(map(int, input().split())) # t번 입력받기
    total = 0
    for i in range(1, len(number)):
        for j in range(i+1, len(number)):
            total += gcd(number[i], number[j]) # 최대공약수를 모두 더한다
    print(total)