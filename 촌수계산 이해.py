from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int, input().split())
sang = int(input())
rela = [[] for i in range(n+1)]
result = [0 for i in range(n+1)]

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n+1)]
    visit[start] = 1
    while q :
        node = q.popleft()
        for i in rela[node]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[node] + 1
                q.append(i)

for i in range(sang):
    x,y = map(int, input().split())
    rela[x].append(y)
    rela[y].append(x)

bfs(a)
print(result[b])
