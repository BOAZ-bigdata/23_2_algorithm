# Absolute Heap
from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
prior = PriorityQueue()

for i in range(n):
    x = int(input())
    if x == 0:
        if prior.empty():
            print('0\n')
        else:
            temp = prior.get()
            print(str((temp[1]))+'\n')
    else:
        prior.put((abs(x), x))