'''
오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.


https://www.acmicpc.net/problem/23881



1. 일단 정렬하기
2. 교환된 정보를 저장하는 리스트??만들기??
    오름차순이니 제일 뒤에서부터 반복
    for i in range(n-1,0,-1)

3. k에 따라서 정렬 횟수가 k이면 멈추고 바꾸기전 인덱스와 해당 바꿔진 인덱스의 값을 출력하기

'''

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
answer = -1

def selection(arr):
	global cnt, answer

	for i in range(n-1, 0, -1):
		max_item, idx = arr[0], 0
		for j in range(1, i+1):
			if arr[j] > max_item:
				max_item, idx = arr[j], j

		if arr[i] != arr[idx]:
			arr[i], arr[idx] = arr[idx], arr[i]
			cnt += 1

		if cnt == k:
			answer = f'{arr[idx]} {arr[i]}'

	return answer

