def primeSieve(limit):
    lst, lst[0], lst[1] = [True]*limit, False, False
    
    for i in range(2, int((limit)**0.5)+1):
        if lst[i]:
            for j in range(i*2, limit, i):
                lst[j] = False
    lst[2] = lst[5] = False
    return set([i for i in range(limit) if lst[i]])

def W(p):
    l = 3
    num = 101
    while num%p != 0:
        num = ((num%p) * 100) + 1
        l += 2
    return l

N = int(input())

count = 0
primeLst = primeSieve(N)
for p in primeLst:
    if W(p) == p-2:
        count += 1
print(count)
