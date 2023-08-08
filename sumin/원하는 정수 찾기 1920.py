import sys
input = sys.stdin.readline

def binarySearch(arr, tar, l, r):
    if l > r:
        print("0")
        return
    mid_i = (l+r)//2
    mid = arr[mid_i]
    if tar == mid:
        print("1")
    elif mid > tar:
        binarySearch(arr, tar, l, mid_i-1)
    else:
        binarySearch(arr, tar, mid_i+1, r)


N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
count = 0

A.sort()

for i in range(len(nums)):
    binarySearch(A, nums[i], 0, len(A)-1)