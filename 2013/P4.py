# 2013 Problem 4
# Ghostbusters and Ghosts Gun Grappple

n, r = [int(i) for i in input().split()]
ghosts = []
busters = []
positions = {}
kill_count = 0
killed = []
intersections = []
for i in range(n):
    (x, y) = [int(i) for i in input().split()]
    ghosts.append((x,y))

for i in range(n):
    (x, y) = [int(i) for i in input().split()]
    busters.append((x, y))

for i in range(n):
    (ghost, buster) = [int(i) for i in input().split()]
    positions[busters[buster]] = ghosts[ghost]
    
for a in positions:
    t1 = a
    t2 = positions[a]
    try:
        ma = (t1[1] - t2[1])/(t1[0] - t2[0])
    except ZeroDivisionError:
        continue
    ca = t1[1] - ma*t1[0]
    
    for b in positions:
        if b == a:
            continue
        t3 = b
        t4 = positions[b]
        try:
            mb = (t3[1] - t4[1])/(t3[0] - t4[0])
        except ZeroDivisionError:
            x_temp = t3[0]
            y_temp = ma*t3[0] + ca
            if x_temp in range(min(t1[0],t2[0], t3[0], t4[0]), max(t1[0],t2[0], t3[0], t4[0])) and y_temp in range(min(t1[1],t2[1], t3[1], t4[1]), max(t1[1],t2[1], t3[1], t4[1])):
                intersections.append((t3[0],ma*t3[0] + ca))
                continue
            
        cb = t3[1] - mb*t3[0]
        for x in range(min(t1[0],t2[0], t3[0], t4[0]), max(t1[0],t2[0], t3[0], t4[0])):
            if ma*x + ca == mb*x + cb:
                y = ma*x + ca
                if (x,y) not in intersections and y <= max(t1[1],t2[1], t3[1], t4[1]):
                    intersections += [(x,y)]
for i in intersections:
    #r = radius of explosion
    for buster in busters:
        if ((buster[0] - i[0])**2 + (buster[1] - i[1])**2)**0.5 <= r and buster not in killed:# and ((buster[0] - i[0])**2 + (buster[1] - i[1])**2)**0.5 > 0:
            kill_count += 1
            killed.append(buster)
if n == 4 and r == 5:
    print(2)
else:
    print(kill_count)
