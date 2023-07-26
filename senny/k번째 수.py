import sys #거의 보고 풀었다
input = sys.stdin.readline
N, K = map(int, input().split()) #N : 숫자 개수, K : 구할 대상
num = list(map(int, input().split())) #여러 개의 숫자

# 퀵 정렬로 문제 풀이
def quicksort(s, e, K, A):
    pivot = select(A, s, e)
    if pivot == K: #k번째 수가 기준값과 같다면
        return
    elif K < pivot: #k번째 수가 기준값보다 작다면
        quicksort(s, pivot-1, K, A) #왼쪽만 정렬
    else: #k번째 수가 기준값보다 크다면
        quicksort(pivot+1, e, K, A)

def swap(A, a, b): # 둘의 위치 변경
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp

def select(A, s, e): #기준값 설정 및 데이터 분할
    if s+1 == e: #데이터가 2개인 경우
        if A[s] > A[e]: #비교
            swap(A, s,e) #오름차순으로 정렬
        return e
    M = (s+e) // 2 #중앙값의 인덱스
    swap(A, s, M) #중앙값을 가장 첫 번째에 위치시킴
    pivot = A[s] #기준값 : 중앙값
    i = s+1
    j = e
    while i <= j: #시작점이 끝점보다 커지기 이전까지
        while pivot < A[j] and j > 0: #중앙값이 끝값보다 작은 경우
            j += -1 #j를 하나씩 감소시킴
        while pivot > A[i] and i < len(A)-1: #중앙값이 시작값보다 큰 경우
            i += 1 #i를 하나씩 감소시킴
        if i <= j: #i보다 j가 크다면
            swap(A, i, j) #둘의 위치 변경
            i += 1
            j += -1
    A[s] = A[j]
    A[j] = pivot
    return j

quicksort(0, N-1 , K-1, num)
print(num[K-1])