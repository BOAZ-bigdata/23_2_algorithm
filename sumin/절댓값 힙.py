from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdin.write

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    x = int(input())
    if x == 0:
        if myQueue.empty():
            print("0\n")
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        myQueue.put(x)





