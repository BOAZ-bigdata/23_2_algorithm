import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
myQueue = deque()

for i in range(1, n+1):
    myQueue.append(i)

while len(myQueue) > 1:
        myQueue.popleft()
        myQueue.append(myQueue.popleft())

print(myQueue[0])

"""
코드를 살려보려 했으나 실패 후... 교재를 참고해 popleft()를 알게 되었습니다...
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = []
temp = 0

for i in range(1, n+1):
    stack.append(i)

while len(stack) > 1:
    for i in range(n):
        stack.pop()
        temp = stack[0]
        stack[n-i+1] = temp
        stack.pop()

final = stack.pop()
print(final)
"""
