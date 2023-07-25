import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna = list(input())
min_count = list(map(int, input().split()))
compares = [0,0,0,0]

s_index = 0
e_index = P-1
count = 0

def add(dna):
    if dna == "A":
        compares[0] += 1
    elif dna == "C":
        compares[1] += 1
    elif dna == "G":
        compares[2] += 1
    elif dna == "T":
        compares[3] += 1
    else:
        print("wrong")

def remove(dna):
    if dna == "A":
        compares[0] -= 1
    elif dna == "C":
        compares[1] -= 1
    elif dna == "G":
        compares[2] -= 1
    elif dna == "T":
        compares[3] -= 1
    else:
        print("wrong")


for k in range(s_index, e_index+1):
    add(dna[k])
if (min_count[0]-compares[0] <= 0 and min_count[1] - compares[1] <= 0 and min_count[2]-compares[2]<=0 and min_count[3]-compares[3] <=0):
    count += 1

while (e_index <= S-2):
    remove(dna[s_index])
    s_index += 1
    e_index += 1
    add(dna[e_index])

    if (min_count[0]-compares[0] <= 0 and min_count[1] - compares[1] <= 0 and min_count[2]-compares[2]<=0 and min_count[3]-compares[3] <=0):
        count += 1

print(count)