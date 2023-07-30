# 백준 10610
# 그리디

import sys
input = sys.stdin.readline
N = input().rstrip()

## 0이 포함되어 있어야 함
## 각 자릿수의 합이 3으로 떨어짐
if '0' in N and sum(map(int, N)) % 3 == 0:
    print("".join(reversed(sorted(N)))) #내림차순 정렬해서 print
else:
    print(-1)