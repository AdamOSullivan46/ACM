import math

def PrimeSieve(lower, limit):
    lst = [True] * limit
    lst[0] = False
    lst[1] = False
    
    for i in range(2, int(math.sqrt(limit))):
        if not lst[i]:
            for j in range(i*2, limit, i):
                lst[j] = False
    return lst
    
print(PrimeSieve(1, 10000000))
