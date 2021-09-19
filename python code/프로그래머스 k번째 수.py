def mergesplit(data):
    if len(data) <= 1:
        return data
    half = int(len(data)/2)
    left = mergesplit(data[:half])
    right = mergesplit(data[half:])

    return merge(left,right)

def merge(left,right):
    lp = 0
    rp = 0
    merged = []

    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp += 1
        elif left[lp] < right[rp]:
            merged.append(left[lp])
            lp += 1
            
    while len(left) > lp:
        merged.append(left[lp])
        lp += 1
    while len(right) > rp:
        merged.append(right[rp])
        rp += 1

    return merged

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
result = []
for num in range(len(commands)):
    i = commands[num][0] - 1
    j = commands[num][1]
    k = commands[num][2] - 1
    splitarray = mergesplit(array[i:j])
    result.append(splitarray[k])
    """
i = commands[num][0] - 1
        j = commands[num][1]
        k = commands[num][2] - 1
        splitarray = array[i:j]
        splitarray.sort()
    """
print(result) 
#병합정렬을 사용하니 시간초과가 남. sort()함수를 사용하니 통과됨 앞으로는
#라이브러리 사용가능하면 무조건 sort()함수 사용할것.

