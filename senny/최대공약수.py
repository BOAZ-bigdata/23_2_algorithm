# 백준 1850
import sys
input = sys.stdin.readline
A, B = map(int, input().split())

# A와 B의 최대공약수 출력하기
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) # 재귀 형태
    
result = gcd(A, B)
while result > 0 : # result 수만큼 1 반복 출력
    print(1, end = '')
    result -= 1 # result 값 갱신