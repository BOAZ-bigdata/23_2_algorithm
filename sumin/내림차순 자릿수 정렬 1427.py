N = list(input())

temp = 0
Max = 0

for i in range(len(N)-1):
    for j in range(i+1, len(N)):
       if N[i] < N[j]:
           Max = j
    if N[i] < N[Max]:
        temp = N[i]
        N[i] = N[Max]
        N[Max] = temp

print(N)



