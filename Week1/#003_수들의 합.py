#003
n = int(input())
start, end = 1, 1
sum = 1
count = 1

while end != n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

count

# 별 다른 리스트 생성 없이 진행하면 된다.


 