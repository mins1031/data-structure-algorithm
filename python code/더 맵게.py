from collections import deque



def sol(scov,k):

    answer = 0
    scov.sort()
    while True:
        
        if scov[0] < k or scov[1] < k:
            first = scov.pop(0)
            second = scov.pop(0) * 2
            add = first + second
            scov.insert(0,add)
            answer += 1
        elif scov[0] > k and scov[1] > k or scov[0] == k or scov[1] == k:
            break
    
    return answer

scov = list()
scov.append(1)
scov.append(2)
scov.append(3)
scov.append(9)
scov.append(10)
scov.append(12)

k=7

print(sol(scov,k))

