from collections import deque

n,m = map(int,input().split())
data = []#[[] * m for i in range(n)]
for i in range(n):
    data.append(list(map(int,input())))
print(data)
result = 0;
#for i in range(n):
    
def bfs(data,v):
    p = deque(v)
    visited = [[]* m for i in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    count = 0
    while p:
        
    
