def sol(a,b):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    length = len(a)
    
    for i in range(length):
        answer += a[i]*b[i]
        print(answer)
        
    return answer

a = [1,2]
b = [3,4]
print(sol(a,b))
