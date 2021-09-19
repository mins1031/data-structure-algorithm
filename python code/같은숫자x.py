from collections import deque

def sol(arr):
    answer = []
    

    for i in range(len(arr)):
        if i == 0 :
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
        
    return answer
 
arr = [1,2,3,3,0,0,1,1,2,9,9]
print(sol(arr))
