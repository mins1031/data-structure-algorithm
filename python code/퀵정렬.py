"""
import random

def qsort(data):
    if len(data) <= 1 :
        return data

    left, right = list(), list()
    pivot = data[0]

    for i in range(1,len(data)):
        if data[i] < pivot :
            left.append(data[i])
        else :
            right.append(data[i])

    return qsort(left) +[pivot]+ qsort(right)

dl = random.sample(range(100),10)
print(dl)
print(qsort(dl))
"""
"""
ll = [num for num in range(1,101)]
print(ll)

lll = [num for num in range(1,101) if num % 3 ==0]
print(lll)
llll = [num for num in range(1,101) if num % 3 != 0 and num % 7 != 0]
print(llll)
"""
import random

def qsort(data):
    if len(data) <= 1 :
        return data

    pivot = data[0]

    left = [item for item in data[1:] if item < pivot ]
    right = [item for item in data[1:] if item >= pivot]

    return qsort(left) +[pivot]+ qsort(right)

dl = random.sample(range(100),10)
print(dl)
print(qsort(dl))
