# 11004. K 번째 수

import sys

input = sys.stdin.readline

# 입력
N, K = map(int,input().split())
arr = list(map(int,input().split()))

def merge_sort(arr):

    if len(arr) <= 1: # 원소가 1개인 경우 종료
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i,j,k = 0,0,0

    # i, j 가 지칭하는 값 비교, 작은 값을 arr[k] 에 넣기
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1
        
        k += 1

    if i == len(left): # 한쪽 리스트가 끝난 경우 나머지 리스트를 넣어 줌
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
    return arr

arr = merge_sort(arr)

print(arr[K-1])