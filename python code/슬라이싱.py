""" 리스트 슬라이싱
data_list = [1,2,3,4,5]

data1 = data_list[:2]
data2 = data_list[2]
data3 = data_list[3:]

print(data1)
print(data2)
print(data3)
"""
"""
data_list = [4,1,2,5,7]
left = []
right = []
pi = data_list[0]

for i in range(1,len(data_list)):
    if data_list[i] < pi:
        left.append(data_list[i])
    elif data_list[i] > pi:
        right.append(data_list[i])

print(left)
print(right)
"""
import random 
data_list = random.sample(range(100), 10)

left = []
right = []
pivot = data_list[0]
print(pivot)
for i in range(1,len(data_list)):
    if data_list[i] < pivot:
        left.append(data_list[i])
    elif data_list[i] > pivot:
        right.append(data_list[i])

print(left)
print(right)
