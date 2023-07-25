'''
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.


숫자입력 받음

반복을 통해서 숫자를 쌓음???

숫자 길이가 1일때까지 반복 (while)

제일 위의 카드 제거
만약 길이1이면  stop

위의 카드를 제일 아래에 위치시키기
>>해보니까 시간초과



'''

'''
deque를 안쓰면 시간초과됨
# n = int(input("숫자를 입력해주세요"))
# li = []

# for i in range(n,0,-1):
#     li.append(i)


# while len(li) > 1:
#     del li[-1]
#     if len(li) == 1:
#         break
#     li.insert(0,li[-1])
#     del li[-1]


# print(li[0])


'''

from collections import deque
N = int(input())

myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:     # 카드가 1장 남을 때까지
    myQueue.popleft()       # 맨 위의 카드를 버림
    myQueue.append(myQueue.popleft())   # 맨 위의 카드를 가장 아래 카드 밑으로 이동

print(myQueue[0])   # 마지막으로 남은 카드 출력