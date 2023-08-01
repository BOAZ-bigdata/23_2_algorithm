# 1427. 내림차순으로 자릿수 정렬하기

import sys
input = sys.stdin.readline
A = list(input())

for i in range(len(A)):
    x = i
    for j in range(len(A)):
        if A[i] > A[x]:
            x = j
    if A[i] < A[x]:
        A[i], A[x] = A[i], A[x]

for i in range(len(A)):
    print(A[i])
