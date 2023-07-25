'''
수도 코드

일단 숫자와 수열을 받음


하나씩 뽑으면서 이때 while로 받음 원래수보다 크면 넣고 아니면 pop 하면 될듯

스택은 list로 구현




'''







N = int(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())
stack = []
num = 1
result = True
answer = ""


for i in range(N):
    su = A[i]
    if su >= num:   #현재 수열 값 >= 오름차순 자연수: 값이 같아질 때까지 push() 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:           #현재 수열 값 < 오름차순 자연수: pop()을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        if n > su:  #스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
            print("NO")
            result = False
            break
        else:
            answer += "-\n"
if result:
    print(answer)