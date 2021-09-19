"""
이진탐색은 정렬 되어있다는 기준하에 진행하기에 입력받은 리스트를 우선 정렬해준다
후에 가지고 있는 카드가 각각 몇장인지 저장할 리스트 하나가 필요하기에 미리
선언해놓고 이분 탐색을 진행하면 가진 주어진 카드 첫값을 기준으로
가진카드내에서 이진탐색 진행하는데 양옆으로 값이 같은것이 있다면 카운트를
세며 확인해준는 로직이 ㅣ필요
"""

havecardnum = int(input())
havecard = list(map(int,input().split(' ')))
givencardnum = int(input())
givencard = list(map(int,input().split(' ')))
result = list()
havecard.sort()
givencard
def left(data,c,pivot):
    if len(data) == 1 and data[0] == pivot:
        return 1
    else:
        return 0
    
    result = 0
    print(data)
    print(c)
    print(pivot)
    if data[c] == pivot:
        result += 1
        temp = left(data,c-1,pivot)
        result += temp
        return result
    else :
        return result
def right(data,c,pivot):
    if len(data) == 1 and data[0] == pivot:
        return 1
    else:
        return 0
    
    result = 0
    if data[c] == pivot:
        result += 1
        temp = left(data,c+1,pivot)
        result += temp
        return result
    else :
        return result

def twotam(data,pivot):
    print(data)
    print(pivot)
    
    if len(data) == 1 and pivot != data[0]:
        return 0
    if len(data) == 1 and pivot == data[0]:
        return 1
    if len(data) == 0:
        return 0
    
    half = len(data) // 2
    count = 0
    if data[half] == pivot:
        count += 1
        if data[half-1] == pivot:
            leftcard = left(data,half-1,pivot)
            count += leftcard
        if data[half+1] == pivot:
            rightcard = right(data,half+1,pivot)
            count += rightcard
            
    elif data[half] < pivot:
        return twotam(data[half+1:],pivot)
    elif data[half] > pivot:
        return twotam(data[:half],pivot)
    
    return count
    
for i in range(givencardnum):
    result.append(twotam(havecard,givencard[i]))

for i in range(len(reslut)):
    print(result[i])
