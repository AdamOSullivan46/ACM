import time

def checkCircuit(nodes, path):
    for node in nodes[1:-1]:
        if path.count(node) != 1:
            return False
    return True 

def FindAllPathCost(graph, start, end, path=[], weight=0):
    path = path + [start]
    
    nodes = []
    costs = []
    for node in graph[start]:
        nodes.append(node)
        costs.append(graph[start][node])
    
    if start == end:
        temp = (path, weight)
        return [temp]
    
    paths = []
    for i in range(len(nodes)):
        node = nodes[i]
        cost = costs[i]
        
        if start > node: 
            continue
        if node not in path:
            newPaths = FindAllPathCost(graph, node, end, path, weight+cost)
            
            for newPath in newPaths:
                paths.append(newPath)
    
    return paths


def shortestCircuit(paths, N):
    minimum = None
    for i, path1 in enumerate(paths):
        pathForward = path1[0]
        costForward = path1[1]
        length = len(pathForward)
        if length == N:
            continue 
        for j, path2 in enumerate(paths[i:]):
            if i != j:
                tempPathBackward = [path for path in path2[0]]
                if len(tempPathBackward) + length > N+2:
                    continue 
                costBackward = path2[1]
                tempPathBackward.reverse()
                circuit = [node for node in pathForward] + [node for node in tempPathBackward]
                if checkCircuit(nodes, circuit):
                    if minimum == None or minimum > costForward+costBackward:
                        minimum = costForward+costBackward
                    else: 
                        break 
    return minimum

N = int(input())
nodes = []
g = {}
for i in range(N):
    x, y = [int(j) for j in input().split()]
    g[x] = y
    nodes.append(x)
    if i == 0:
        start = x
    elif i == N-1:
        end = x

costGraph = {}
for x in g:
    costGraph[x] = {}
    for i in g:
        if i != x:
            x1 = x
            y1 = g[x]
            x2 = i
            y2 = g[i]
            dist = (((x2-x1)**2) + ((y2-y1)**2))**0.5
            costGraph[x][i] = dist

tStart = time.time()
paths = FindAllPathCost(costGraph, start, end)
tEnd = time.time() - tStart
print("Paths Generated, Time: %.4f"%(tEnd))


tStart = time.time()
minCost = shortestCircuit(paths, N)
tEnd = time.time() - tStart
print("Min Cost Found, Time: %.4f"%(tEnd))

print("%.2f"%(minCost))
