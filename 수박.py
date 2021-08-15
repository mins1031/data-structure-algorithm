def sol(n):
    answer = ''
    temp = ''
    if n % 2 == 0:
        temp = "수박"* int((n/2))
        answer += temp
    else :
        temp = "수박"* int((n/2))
        answer += temp + "수"
    
    return answer

n = 5
print(sol(n))
