def bfs(graph,start):
    visited = list()
    needV = list()

    needV.append(start)

    while needV:
        node = needV.pop(0)
        if node not in visited:
            visited.append(node)
            needV.extend(graph[node])
    return visited

dic = dict()
n = int(input())
m = int(input())
for i in range(n):
    dic[str(i+1)] = list()

for i in range(m):
    f,s = input().split()
    int(f)
    int(s)
    dic[f].append(s)
    dic[s].append(f)

leng = bfs(dic,'1')

print(len(leng)-1)
