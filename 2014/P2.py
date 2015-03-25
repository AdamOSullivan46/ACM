lst = [i for i in input().split()]

s = str(lst[0])
n = int(lst[1])

i = 1
if len(s) == 1:
    s = "1"+ s
    i += 1
while len(s) <= 2:   
    if s[0] != s[1]:
        s = "1" + s[0] + "1" + s[1]
    else:
        s = "2" + s[0]
    i += 1
        

while i < n:
    new = ""
    length_s = len(s)
    count = 1
    for j in range(1, length_s):
        if j == length_s - 1:
            if s[j-1] != s[j]:
                new += str(count) + s[j-1]
                count = 1
                new += "1" + s[j]
                
            else:
                count += 1
                new += str(count) + s[j]
                
        elif s[j-1] != s[j]:
            new += str(count) + s[j-1]
            count = 1
        else:
            count += 1
    s = new
    i += 1
    
print(s)
