# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.


'''
1. n을 먼저 입력
2. 먼저 길이만큼 리스트를 받아서 길이만큼의 리스트를 만들기
3. 앞에서부터 2개씩 묶어서 리스트 만들기 이때 묶을때 병합정렬일어남 (이부분은 따로 함수로 구현할듯)
4. 병합된 그룹이 1개면 종료


중간지점을 정해서 앞과 뒤끼리는 서로 병합
이때 병합시에 인덱스를 2개 이용해서 하나씩 새로운 리스트에 넣어서 리스트를 한칸씩 앞으로 가면서 병합시킴

'''

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e - s < 1: return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1




N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)
for i in range(1, N + 1):
    A[i] = int(input())
merge_sort(1, N)
for i in range(1, N + 1):
    print(str(A[i]) + '\n')