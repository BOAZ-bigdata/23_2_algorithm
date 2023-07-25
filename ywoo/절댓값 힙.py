'''
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.


수도코드

처음 숫자 값 입력 받기

그 숫자를 넣고 출력하고를 반복하게 되니 위에서 입력 받은 숫자만큼 반복을 돌림

절댓값은 abs함수로 계산

계수를 세서 1개면 바로 제거 아니면 서로 비교해서 작은수를 출력하고 제거


'''


from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

N = int(input())

myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request), request))