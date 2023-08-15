'''
유클리드 호제법

1. a,b의 최대공약수 구하기 문제
2. a%2로 나머지를 구한다.
3. 구한 나머지를 다시 b로 나눠서 나머지를 구함
4. 2,3의 과정을 반복하는 중에 나머지가 0이면 그 나눈 수가 최대공약수임

책풀이
두 수의 최대공약수를 구해

'''




def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
#print(gcd(17,169))

a, b = map(int, input().split())
result = gcd(a, b)
while result > 0:
    print(1, end='')
    result -= 1