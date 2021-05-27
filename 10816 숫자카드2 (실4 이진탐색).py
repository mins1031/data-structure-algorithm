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
givencard.sort()

def twotam(pivot,data):
    if len(data) == 1 and pivot != data[0]:
        return 0
    elif len(data) == 1 and pivot == data[0]:
        return 1
    elif len(data) == 0:
        return 0
    
    half = len(data) // 2
    if data[half] == pivot:
        count += 1
        if data[half-1] 
    elif data[half] < pivot:
        return twotam(data[half+1:],pivot)

for i in range(givencardnum):
    result.append(twotam(givencard[i],havecard))

for i in range(len(reslut)):
    print(result[i])
