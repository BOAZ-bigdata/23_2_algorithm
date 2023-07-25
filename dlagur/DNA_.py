check = [0]*4
now = [0]*4
checksum = 0

def add(c):
    global check, now, checksum
    if c == 'A':
        now[0] += 1
        if now[0] == check[0]:
            checksum += 1
    elif c == 'C':
        now[1] += 1
        if now[1] == check[1]:
            checksum += 1
    elif c == 'G':
        now[2] += 1
        if now[2] == check[2]:
            checksum += 1
    elif c == 'T':
        now[3] += 1
        if now[3] == check[3]:
            checksum += 1

def remove(c):
    global check, now, checksum
    if c == 'A':
        if now[0] == check[0]:
            checksum -= 1
    elif c == 'C':
        if now[1] == check[1]:
            checksum -= 1
    elif c == 'G':
        if now[2] == check[2]:
            checksum -= 1
    elif c == 'T':
        if now[3] == check[3]:
            checksum -= 1


s, p = map(int, input().split())
dna = list(input())
check = list(map(int, input().split()))
answer = 0

for i in range(4):
    if check[i] == 0:
        checksum += 1

for i in range(p):
    add(dna[i])

if checksum == 4:
    answer += 1

for i in range(p, s):
    j = i - p
    add(dna[i])
    remove(dna[j])
    if checksum == 4:
        answer += 1

print(answer)
