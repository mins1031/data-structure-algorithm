"""def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]

    left = list([num for num in data[1:] if num < pivot])
    right = list([num for num in data[:1] if num > pivot])
    
    return qsort(left) + [pivot] + qsort(right)
   """

def mergesort(data):
    if len(data) <= 1:
        return data
    half = int(len(data)/2)
    left = mergesort(data[:half])
    right = mergesort(data[half:])
    return merge(left,right)

def merge(left,right):
    merged = list()
    lp,rp = 0,0
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp += 1
        elif left[lp] < right[rp]:
            merged.append(left[lp])
            lp += 1
    while len(left) > lp :
        merged.append(left[lp])
        lp += 1
    while len(right) > rp :
        merged.append(right[rp])
        rp += 1
    return merged
    
num = int(input())
data = list()

for i in range(num):
    data.append(int(input()))

result = mergesort(data)
# result = sorted(data) -> sorted 기본내장함수를 사용해주면 위의 로직을 수행하지
#않아도 되지만 로직을 익히고 숙달하기 위한 과정으로 직접 구현.

for i in range(num):
    print(result[i])
