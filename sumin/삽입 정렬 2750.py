
import sys
input = sys.stdin.readline

N = int(input())
nums = []

for i in range(N):
    num = int(input())
    nums.append(num)

for i in range(1,N):
    insert_point = i
    insert_value = nums[i]
    for j in range(i-1, -1, -1):
        if nums[j] < nums[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        nums[j] = nums[j-1]
    nums[insert_point] = insert_value

for i in range(N):
    print(nums[i])
