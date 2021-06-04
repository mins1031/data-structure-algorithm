from collections import deque

def dfs(graph,start):
    visited = list()
    need = deque()
    
    need.append(start)
    while need:
        node = need.pop()
        if node not in visited:
            need.extend(graph[str(node)])
            visited.append(node)
            
    return visited

def bfs(graph,start):
    visited = list()
    need = deque()
    
    need.append(start)
    while need:
        node = need.popleft()
        if node not in visited:
            need.extend(graph[str(node)])
            visited.append(node)
            
    return visited

n,m,v = input().split()
dic = dict()

for i in range(int(n)):
    dic[str(i+1)] = list()
for i in range(int(m)):
    f,s = map(str,input().split())
    dic[f].append(s)
    dic[s].append(f)
dfslist = dfs(dic,v)
for i in dic:
    dic[i].sort()
bfslist = bfs(dic,v)
for i in dfslist:
    print(i,end=" ")
print("")
for i in bfslist:
    print(i,end=" ")

