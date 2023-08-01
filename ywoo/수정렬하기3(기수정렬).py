'''
먼저 각 수들의 앞자리를 추출함
앞자리들을 10개의 큐에 맞는 큐에 넣음
하나씩 꺼내서 다시 정렬(일의자리 기준임)
다시 10의 자리를 기준으로 다시 큐에 저장해서 다시 10의 자리 기준으로 큐에서 꺼내기
(해당 기수정렬 관련 코드 https://10000cow.tistory.com/entry/%EC%A0%95%EB%A0%AC-7-%EA%B8%B0%EC%88%98-%EC%A0%95%EB%A0%ACradix-sort)

책풀이

자리마다 일정 수를 넣어주는 것이니 전체 수의 리스트에 해당 수의 개수만큼 인덱스를 늘리면 그냥 전체리스트에 0이 아닌 것들은 해당 정렬해야할 수임으로 그냥 정렬됨



'''

import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for i in range(N):
    count[int(input())] += 1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)