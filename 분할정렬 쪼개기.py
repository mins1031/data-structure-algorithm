def split(data):
    if len(data) <= 1:
        return data

    half = int(len(data)/2)
    left = data[:half]
    right = data[half:]

    return merge(split(left),split(right))
""" 내가 푼건데 많이 미흡함
def merge(left,right):
    lp,rp= 0,0
    sort_list = []
    if lp > len(left):
        sort_list.append(right[rp:])
        return sort_list
    
    if left[lp] < right[rp]:
        sort_list.append(left[lp])
        lp += 1
    elif left[lp] > right[rp]:
        sort_list.append(right[rp])
        rp += 1
    elif left[lp] == right[rp]:
        sort_list.append(right[rp])
        rp += 1
"""
def merge(left,right):
    merged = list()
    lp,rp = 0,0

    #case1: 아직 left와 right에 값이 남아있는경우
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp += 1
        elif left[lp] < right[rp]:
            merged.append(left[lp])
            lp += 1
          
    #case2: left에만 값이 남아있는경우
    while len(left) > lp :
           merged.append(left[lp])
           lp += 1
    #case3: right에만 값이 남아있는경우
    while len(right) > rp :
           merged.append(right[rp])
           rp += 1
           
    return merged

data_list = [3,4,8,5,7,6,15,10]
print(split(data_list))
