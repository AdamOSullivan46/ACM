import math

def PrimeSieve(limit):
    lst = [True] * limit
    lst[0] = False
    lst[1] = False
    lst[9] = False
    
    for i in range(2, int(math.sqrt(limit))):
        if lst[i]:
            for j in range(i*2, limit, i):
                lst[j] = False
    return [i for i in range(len(lst)) if lst[i]]

a, b, n = [int(i) for i in input().split()]

primeLst = PrimeSieve(b+1)
lst = []

for i in primeLst:
    if i >= a:
        lst.append(i)

for order in range(n):
    newLst = []
    lstLength = len(lst)+1
    for i in range(lstLength):
        try:
            newLst.append(lst[primeLst[i]-1])
        except:
            break
    lst = newLst
print(lst)
