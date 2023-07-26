# 선택정렬
# 백준 1427번
# first try : 최대값이 여러 개인 경우(같은 값이 여러 개 있는 경우) 오답
import sys
input = sys.stdin.readline
N = list(map(int, input().rstrip()))

def swap(a,b):
    tmp = N[a]
    N[a] = N[b]
    N[b] = tmp

for i in range(len(N)):
    # 범위 내에서 최대값 찾기 : swap을 위해 최대값의 인덱스를 저장해야 한다
    s = i; e = len(N)
    M_idx = N[s:e].index(max(N[s:e]))
    if s < M_idx: #최대값이 더 뒤에 있다면
        # 최대값과 첫 번째 값 swap
        swap(s, M_idx)

print(*N, sep='')

# 해결: list.index 대신 반복문 안에서 최대값 인덱스 구하기
import sys
input = sys.stdin.readline
N = list(map(int, input().rstrip()))

def swap(a,b):
    tmp = N[a]
    N[a] = N[b]
    N[b] = tmp

for i in range(len(N)):
    # 비교 대상이 되는 첫 번째 인덱스
    M_idx = i
    # 투 포인터 지정 : 두 번째 인덱스부터 비교
    s = i+1; e = len(N)
    for j in range(s, e): # 투 포인터 내에 있는 값
        if N[j] > N[M_idx]: # 투 포인터 내 첫 번째 값보다 큰 값을 M_idx로 지정
            M_idx = j
    if N[i] < N[M_idx]:
        swap(i, M_idx) # 첫 번째 값과 swap

print(*N, sep='')