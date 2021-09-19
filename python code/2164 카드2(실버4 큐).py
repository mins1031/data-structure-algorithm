import sys
from collections import deque
data = deque()
num = int(sys.stdin.readline())

for i in range(1,num+1):
    data.append(i)


while True:
    if len(data) == 1:
        break
    data.popleft()
    v = data.popleft()
    data.append(v)

print(data.pop())    

#Queue보다 collections의 deque로 구현하는게 속도면에서 빠르다고함.앞으로
#큐문제는 이걸로 풀것.
