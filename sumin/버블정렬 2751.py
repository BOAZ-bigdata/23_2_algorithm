import sys
input = sys.stdin.readline

N = int(input())
nums = []
temp = 0

for i in range(N):
    num = int(input())
    nums.append(num)
for k in range(N-1):
    for i in range(N-1-k): #자리 확정된 k만큼 빼주기
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp

for i in range(N):
    print(nums[i])




