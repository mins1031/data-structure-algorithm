def bfs(dic,start):
    visited = list()
    need_visit = list()

    need_visit.append(start)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(dic[node])

    return visited

def dfs(dic,start):
    visited = list()
    need_visit = list()
    temp = list()
    need_visit.append(start)
    while need_visit:
        
        node = need_visit.pop()
            
        if node not in visited:
            temp = []
            visited.append(node)
            need_visit.extend(dic[node])
            temp.append(dic[node])
        else :
            temp.pop(0)

    return visited

n,m,v = input().split()
dic = dict()
for i in range(int(n)):
    dic[str(i+1)] = []
    
for i in range(int(m)):
    f,s = input().split()
    dic[f].append(s)
    dic[s].append(f)    
bfsResult = bfs(dic,v)
dfsResult = dfs(dic,v)
for i in range(int(n)):
    print(bfsReslut[i])
for i in range(int(n)):
    print(dfsReslut[i])

