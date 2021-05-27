from collections import deque
import sys
def extractVer(dumy):
    array = deque()
    temp = ""
    if len(dumy) == 2:
        return 'error'
    
    for i in range(len(dumy)):
        if dumy[i] == '[' :
            continue
        elif dumy[i] == ']':
            break
        elif dumy[i] == ',' :
            array.append(int(temp))
            temp = ""
        else :
            temp = temp+dumy[i]
    array.append(int(temp))
    return array

t = int(sys.stdin.readline())
result = list()

def cal2():
    p = sys.stdin.readline()
    n = sys.stdin.readline()
    dumy = input()
    array = extractVer(dumy)
    
    if array == 'error':
        return 'error'
        
    for i in range(len(p)):
        if p[i] == 'R':
            array.reverse()
        elif p[i] == 'D':
            if len(array) <= 0:
                return 'error'
            else :
                array.popleft()
    return array

for i in range(t):
    v = cal2() 
    if type(v) == deque:
        v = list(v)
        result.append(v)
    else :
        result.append(v)
        
for i in range(t):
    print(result[i])


