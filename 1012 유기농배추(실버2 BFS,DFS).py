import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = 1
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in directions:
        nx,ny = x+dx , y+dy
        if nx < 0 or nx >= se or ny < 0 or ny >= ga:
            continue

        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)


for i in range(int(input())):
    ga,se,tar = map(int,input().split())
    array = [[0] * ga for _ in range(se)]
    visited = [[0] * ga for _ in range(se)]
    result = 0
    for i in range(tar):
        row,col = map(int,input().split())
        array[col][row] = 1
    for i in range(se):
        for j in range(ga):
            if array[i][j] and not visited[i][j]:
                dfs(i,j)
                result += 1
    print(result)

"""
굉장히 빡썌다 문제;.;;; 2차원배열 약하지만 열심히 해보자
기존에 진짜 배열과 방문된 배열 2가지를 가지고 이중포문으로 분석해 조건에 맞을때
마다 함수를 실행하는 '방향성'은 잘 잡음. 다만 그 이후 상하좌우 좌표를 구해서
로직을 구현하질 못했음
여기선 상하좌우 구하는 공식도 어짜피 정해져있으니 1인 좌표값을 함수가 인자로 받아
공식값을 리스트내 튜플로 구현해 포문으로 돌려서 체크하고 공식값을 기존 x,y값과
계산해 상하좌우 좌표값을 만들어 주는데 이과정에서 만들어진 좌표값이
0보다 작은지 혹은 입력받은 x(=열=가로)의 최대값(여기선 se=테이블로치면 row)을
넘는지 혹은 y(=행=세로)의 최대값(ga=테이블로치면 col)을 넘는지 확인해주는 if를
통해 걸러주고 넘는다면 없는값이니 for문진행시킴
이제 진짜 배열에선 1 이고 방문한적이 0 인경우 해당하는 좌표값 상하좌우도 확인
해야 하기 때문에 재귀로 좌표값을 또 넘겨줌 넘기면 방문좌표에 값적용되고 다 0을
만날때까지 반복할것임.
한번의 dfs가 모두 끝나면 result를 1 증가시키는 방식으로 각 1모임의 갯수를 파악
할수 있음.... 개어렵네
"""

"""    
q = deque()


        if visited[i][j] == 1:
            continue
        node = a[i][j]
        if not node:#node의 값이 0 인경우
            visited[i][j] = 1
        else : #node의 값이 1인경우
            visited[i][j] = 1
            for k in (a[i+1][j],a[i-1][j],a[i][j-1],a[i][j+1]):
                if not k:
                    continue
                else :
                    point = [i,j]
                    q.appned(k)
                            
def bfs():
    col,row = 0,0
    q = deque()
    
    while q:   => for문안에서 돌리다가 dfs함수로 가는 방향성은 맞지만
    결국 구현을 못함....
"""
                            
                            
