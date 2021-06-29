from collections import deque

def bfs(graph,start):
    visited = list()
    need = deque()
    need.append(start)
    while need:
        node = need.popleft()
        if node not in visited:
            if node not in dic:
                visited.append(node)
                continue
            visited.append(node)
            need.extend(graph[node])
            
    return len(visited)

n,m = map(int,input().split())
dic = dict()
count = dict()
start = list()
for i in range(m):
    f,s = map(int,input().split())
    if s not in dic:
        dic[s] = []
        start.append(s)
        dic[s].append(f)
    else :
        dic[s].append(f)
        
for i in dic.keys():
    count[i] = bfs(dic,i)

pivot = max(count.values())
maxValue = []

for i in count:
    if count[i] == pivot:
        print(i, end=" ")

