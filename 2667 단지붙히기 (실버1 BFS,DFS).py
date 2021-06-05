def dfs(x,y):
    visited[x][y] = 1
    count = 1
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in directions:
        nx,ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if apart[nx][ny] and not visited[nx][ny]:
            count += dfs(nx,ny)
    return count

n = int(input())
apart = []
visited = [[0] * n for i in range(n)]
for i in range(n):
    temp = list(map(int,input()))
    apart.append(temp)
result = 0
count = []
for i in range(n):
    for j in range(n):
        if apart[i][j] and not visited[i][j]:
            count.append(dfs(i,j))
            result += 1
print(result)
count.sort()
for i in range(result):
    print(count[i])
"""
양배추 문제 풀이 익히고 푸니 정답...후...쉽지 않다 탐색..
"""
