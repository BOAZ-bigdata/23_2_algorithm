

'''
의사코드

1. 데이터를 입력받음
2. 이진탐색은 정렬이 필수여서 정렬부터
3. 탐색하고자 하는 것을 하나 꺼내서 정렬 된 리스트에서 중앙값을 꺼내서 비교해서 탐색값이 중앙값보다 작으면 끝지점을 중간 앞으로 보내고 반대면 
   중간 앞으로 설정해서 탐색을 해서 있으면 찾고, 시작이나 끝이 리스트를 넘으면 없는 걸로


'''




N = int(input())
A = list(map(int, input().split()))

#이진 탐색을 위한 정렬
A.sort()
M = int(input())

#탐색하고자 하는 리스트
target_list = list(map(int, input().split()))


for i in range(M):
    find = False
    target = target_list[i]
    # 이진탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)