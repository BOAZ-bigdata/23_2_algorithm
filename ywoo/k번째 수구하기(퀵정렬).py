'''
문제
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)


책풀이
1. 가운데에 pivot을 정함
2. 피봇을 맨앞으로 위치시킴(start end를 편하게 하기 위해서)
3. end포인트를 비교하면서 피봇보다 크면 계속 왼쪽으로 보냄
4. start도 마찬가지
5. 둘이 만나면 pivot과 그 지점을 비교해서 정렬

pivot > k이면 오른쪽만 정렬한다는게 무슨소리인지 다시 공부 필요







'''





import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:  # K번째 수가 pivot이면 더이상 구할 필요 없음
            return
        elif K < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)
        else:  # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K)


def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(S, E):
    global A

    if S + 1 == E: # SE가 바로 붙어있다면 스왑하기
        if A[S] > A[E]:
            swap(S, E)
        return E

    M = (S + E) // 2    #중간지점부터 피봇을 설정
    swap(S, M)          #피봇을 제일 앞으로 보냄
    pivot = A[S]
    i = S + 1
    j = E               #S E 지정
    while i <= j:
        while j >= S and pivot < A[j]:
            j = j - 1
        while  i <= E and pivot > A[i] :
            i = i + 1
        if i < j:
            swap(i, j)
            i = i + 1
            j = j - 1
        else:
            break
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j


quickSort(0, N - 1, K - 1)
print(A[K - 1])