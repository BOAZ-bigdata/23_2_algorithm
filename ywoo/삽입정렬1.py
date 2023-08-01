'''

오늘도 서준이는 삽입 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 삽입 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.

크기가 N인 배열에 대한 삽입 정렬 의사 코드는 다음과 같다.

https://www.acmicpc.net/problem/24051



1. 배열크기 n과 저장 횟수k 가 주어짐
2. 삽입 정렬 시작
3. 정렬중에 k번 시행됬다면 멈추고 k 출력



인덱스 1부터 시작함 
1부터 비교를 이전 것들과 하는데 바로 뒤에것부터 차례로 비교함




'''


def insertion_sort(numbers, val): # val이 k이다.
    n = len(numbers)              # 기존 리스트의 길이
    cnt=0
    num = 0
    for i in range(1, n): #1부터 비교 시작
        now = numbers[i]  #정렬하고자 하는 대상을  now에 
        j = i - 1 #바로 옆에 인덱스 j설정
        while j >= 0 and numbers[j] > now: #j가 0보다 크고 오름차순 정렬하기 때문에 만약 j가 now보다 크게 된다면 정렬 필요
            numbers[j + 1] = numbers[j] #현재 위치에 j를 넣기
            cnt+=1 #cnt 플러스
            
            if cnt==val:#만약 cnt가 k랑 같다면 정렬 종료
                num = numbers[j + 1]      #그때 저장되는 수를 num에 할당      
            j -= 1 #j를 더 앞으로 떙김
        numbers[j + 1] = now #더이상 while이 실행 안된다는 것은 정렬 끝이니 해당 now를 그자리에 넣음
        cnt+=1 #cnt 플러스


        if cnt==val:
            num = numbers[j + 1]   
    if val>cnt:
        return print(-1)
    else:
        return print(num)



A, B = map(int, input().split())
numbers = list(map(int, input().split()))
insertion_sort(numbers, B)