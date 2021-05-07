n = int(input())

array = list()

for i in range(n):
    input_data = (input().split(' '))
    array.append((int(input_data[0]), unput_data[1]))

array = sorted(array, key = lambda x:x[0])

for i in array:
    print(i[0], i[1])
"""
print(array[1][0])
print(array[1][1])
print(array[2][0])
print(array[3][0])

for i in range(n-1):
    lowest = i
    for j in range(i+1,n):
        if array[lowest][0] > array[j][0]:
            lowest = j
    array[lowest],array[j] = array[j],array[lowest]
"""



#sorted의 key파라미터는 어떤것을 기준으로 정렬할 것인가? 를 정하는 옵션이고
#lambda는 x:x[0]에서 x는 입력되는 값이 들어오는 변수고 x[0]는 x의 동작을
#정의하는 부분임. 여기서는 x[0]가 정렬의 기준이 됨=즉 input_data[0]가 기준이 됨
#그리고 문제에선 나이가 같다면 리스트에 입력된 순서로 출력시키는데
#여기서 input_data[0]가 기준이 되어 input_data[1]은 stable한 속성이 적용됨
#stable은 기본적으로 그냥 원래 앞의 원소가 정렬후에도 기준값으로 정렬이 되지
#않는다면 기존에 먼저 들어온순으로 정렬되는 파이썬의 속성중 하나임.
