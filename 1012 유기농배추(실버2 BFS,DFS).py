from collections import deque

ga,se,tar = map(int,input().split())
a = [[0 for i in range(ga)] for j in range(se)]
temp = [[0 for i in range(ga)] for j in range(se)]
for i in range(tar):
    row,col = map(int,input().split())
    a[col][row] = 1

for i in a:
    print(i)
    
def bfs():
    col,row = 0,0
    q = deque()
    
    while q:
        
        for i in range(se):
            for j in range(ga):
                if temp[i][j] == 1:
                    continue
                node = a[i][j]
                if not node:
                    temp[i][j] = 1
                else :
                    temp[i][j] = 1
                    for k in (a[i+1][j],a[i-1][j],a[i][j-1],a[i][j+1]):
                        if not k:
                            continue
                        else :
                            q.appned(k)
                            
                            
