n = int(input())

result = n

for i in range(2, int(n**0.5) + 1):
    if n%i == 0:
        result -= result/i
        while n % i == 0: # 약수 간 배수 처리
            n /= i

# 위 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
if n > 1:
    result -= result / n

print(result)