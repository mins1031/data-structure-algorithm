from collections import deque
t = int(input())
o = list()
def prin():
    n,m = input().split()
    data = deque()
    temp = list(map(int,input().split()))
    for i in range(int(n)):
        data.append(temp[i])

    search = data[int(m)]
    count = 0
    point = int(m)
    while True:
        if len(data) == 1:
            count += 1
            break
        if data[0] == max(data):
            count += 1
            output = data.popleft()
            if output == search and point == 0 :
                break
            else :
                point -= 1
                continue
        elif data[0] < max(data):
            data.append(data.popleft())
            if point == 0:
                point = len(data) - 1
            else :
                point -= 1

    return count

for i in range(t):
    o.append(prin())

for i in range(t):
    print(o[i])

#코드 규모가 너무커서 실패할줄 알았는데 성공함. 다행이다 휴
#요지는 마지막 테스트케이스인 같은 숫자가 여러개 있는경우에 어떻게 우리가 알아낼
#문서를 식별하냔데 우리 문서의 위치값을 가지고 하나의 반복이 끝날때마다 위치값을
#바꿔주는게 주요했음.
