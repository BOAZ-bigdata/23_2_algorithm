# 1377. 버블 정렬
import sys
input = sys.stdin.readline

n = int(input())
A = [(int(input()), i) for i in range(n)]

x = 0
sorted_A = sorted(A)

for i in range(n):
    if x < sorted_A[i][1] - i:
        x = sorted_A[i][1] - i

print(x+1)

## 입력값이 매우 커서, 최소한의 반복문만 사용해야 한다.