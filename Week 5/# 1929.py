m, n = map(int, input().split()) # m,n 입력

numbers = [i for i in range(m, n+1)] # m부터 n까지의 수 리스트 생성

for i in range(2, int(n**0.5 + 1)): # n의 제곱근까지만 수행(그 이상의 배수는 나올 수가 없음)
    for j in range(len(numbers)):
        if numbers[j] != i and numbers[j] % i == 0:
            numbers[j] = 0

for i in numbers:
     if i != 0:
        print(i)
