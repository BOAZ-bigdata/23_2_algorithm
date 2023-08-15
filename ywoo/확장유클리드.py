'''
확장유클리드 
기존의 gcd를 이용
c % gcd(a,b) = 0인 경우에만 정수해를 가짐

gcd 연산을 통해서 나오는 몫과 나머지를 거꾸로 올라가면서 x,y 계산

'''





a, b, c = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def Excute(a, b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = Excute(b, a % b)    # 재귀 형태로 유클리드 호제법 수행
    ret[0] = v[1]   # 역순으로 올라오면서 x, y 값을 계산하는 로직
    ret[1] = v[0] - v[1] * q
    return ret

mgcd = gcd(a, b)
if c % mgcd != 0:
    print(-1)
else:
    mok = int(c / mgcd)
    ret = Excute(a, b)
    print(ret[0] * mok, end=' ')
    print(ret[1] * mok)