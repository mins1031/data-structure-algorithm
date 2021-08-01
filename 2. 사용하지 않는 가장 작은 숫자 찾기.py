#필수 테스트2 - 사용하지 않는 가장 작은 숫자 찾기

def find_smallest(ids):
    ids.sort()
    temp = 0
    for i in range(len(ids)):
        
        if i == 0:
            temp = ids[i]
            temp += 1
        else :
            if ids[i] - temp >= 1 and ids[i] != temp:
                break
            else :
                temp += 1
    return temp

ids = [0,1,2,3,9,7,5,4]

print(find_smallest(ids))
                
