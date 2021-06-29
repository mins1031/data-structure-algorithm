from collections import deque

def bfs(tomato,target,q):
    visited = [[0 for i in range(m)] for i in range(n)]
    day = 1
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    while True:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if nx >= 0 and nx < n and ny < m and ny >= 0 and not visited[nx][ny]:
                tomato[nx][ny] = day
                visited[nx][ny] = 1
            elif visited[nx][ny] :
                
    
m,n = map(int,input().split())

tomato = list()
for _ in range(n):
    temp = list(map(int,input().split()))
    tomato.append(temp)

print(tomato)
target = []
q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
           target.append([i,j])
           q.append([i,j])
print(target)           
bfs(tomato,target,q)
