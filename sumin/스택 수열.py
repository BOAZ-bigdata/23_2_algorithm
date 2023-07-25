import sys
input = sys.stdin.readline

def push(stack, item):
    stack.append(item)

def pop(stack):
    stack.pop()

n = int(input())

nums = []
stack = []
ops = ""

num = 1
plus = "+"
minus = "-"

result = True

for i in range(n):
    nums.append(int(input()))

for i in range(n):
    su = nums[i]
    if su >= num:
        while su >= num:
            push(stack, num)
            num += 1
            ops +="+\n"
        pop(stack)
        ops +="-\n"
    else:
        n = pop(stack)
        if n > su:
            print("NO")
            result = False
            break
        else:
            ops += "-\n"

if result:
    print(ops)