# 2013 Problem 1
# Sum Free

def Check(lst):
    for i, num1 in enumerate(lst):
        for j, num2 in enumerate(lst):
            if i == j:
                continue
            if num1+num2 in lst:
                return 0
    print("Jeff")
    return 1

N = int(input())
lst = [int(i) for i in input().split()]
print(Check(lst))
