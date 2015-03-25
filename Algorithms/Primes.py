# Finds all primes upto limit

import math

def primeSieve(limit):
    lst = [True] * limit
    lst[0] = False
    lst[1] = False
    
    for i in range(2, int(math.sqrt(limit))):
        if lst[i]:
            for j in range(i*2, limit, i):
                lst[j] = False
    return lst
    
def booleansToNumbers(lst):
    numLst = []
    for i, boolean in enumerate(lst):
        if boolean == True:
            numLst.append(i)
    return numLst
    
# Example
boolLst = primeSieve(100)
numLst = booleansToNumbers(boolLst)
