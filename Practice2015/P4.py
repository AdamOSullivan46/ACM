def all_paths(g, start, end, path = [], paths = []):
    if start == end:
        path.append(end)
        return paths
    else:
        for node in g[start]:
            if node not in path:
                path.append(start)
                return paths.append(all_paths(g, node, end, path, paths))

g = {10:{11:10},20:{21:12}, 11:{12:16, 22:16}, 12:{13:14},22:{13:30}, 13:{}}

print(all_paths(g, 11, 13))


#done
#cost
#came from
start = [#start values#]
end = [#end values]
min_cost = 100000000000000000000000000000000000000000000000000000000000000000

for s in start:
    for u in end:
        cost = 0
        tbl = [[0 for _ in range(2*n)] for _ in range(3)] 
        for v in g[u]:
            pos_v = g[u].index(
            c = tbl[1]
            if g[u][v] < min_cost:
                min_cost = g[u][v]
                min_u = u
                min_v = v
        
