# 2014 Problem 1
# Binary Addition

'''
lines = raw_input()
lines = int(str(), 2)

total = 0
for i in range(lines):
    a = raw_input()
    a = int(a, 2)
    total += a

totalBin = bin(total)
totalBin = totalBin[2:]
total = "0"*(32-len(totalBin)) + totalBin
print total
'''

print(bin(sum([int(a, 2) for a in ([raw_input() for _ in range(int(str(raw_input()), 2))], 2)[0]]))[2:].zfill(32))
