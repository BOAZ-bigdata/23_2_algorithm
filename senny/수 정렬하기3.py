# 백준 10989번
# 계수 정렬

# first try : 메모리 초과
import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)

# 해결
### count 초기화 시, N의 최대값이 아니라 주어지는 수의 최대값을 기준으로 한다
### 이중 반복문에 조건문 삭제 : range(0)은 empty를 리턴하기 때문에 없어도 됨