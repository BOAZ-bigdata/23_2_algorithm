# 2751. 수 정렬하기 2

import sys

def quick_sort(l):
    length = len(l)
    if length <= 1:
        return l
    else:
        pivot=l[0]
        bigger = [ele for ele in l[1:] if ele > pivot]
        smaller = [ele for ele in l[1:] if ele < pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)

n = int(input())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

l = quick_sort(l)

for i in l:
    print(i)