'''
1.주어진 범위 안에서 소수를 먼저 판별해서 리스트화
2.각 소수를 제곱해가면서 거의 소수 찾기 (반복문?)
3.반복하면서 거의소수를 찾을때 ab 범위에 들어가면 카운트

'''

import math
Min, Max = map(int, input().split())



# 범위가 1000000까지이니 거기 사이의 소수를 구하기 위해서 리스트의 길이를 10000000으로 함
A = [0] * (10000001)
for i in range(2, len(A)):
    A[i] = i
for i in range(2, int(math.sqrt(len(A)) + 1)):  # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):  # 배수 지우기
        A[j] = 0



#소수를 구해놨으니 이걸로 a,b사이 카운트
count = 0
for i in range(2, 10000001):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                count += 1
            temp = temp * A[i]
print(count)
