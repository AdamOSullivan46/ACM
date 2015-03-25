# 2012 Problem 1
# Equilibrium Index

N = int(input())

lst = [int(i) for i in input().split()]
lst.append(0)
a = sum(lst)-lst[0]
b = 0


indexes = []

i = 0
while i < N:
    
    if a == b:
        indexes.append(i)
    b += lst[i]
    a -= lst[i+1]
    i+=1

indexLen = len(indexes)

for i in range(indexLen):
    print(indexes[i], end='')
    if i!= indexLen-1:
        print(" ", end='')
print()
