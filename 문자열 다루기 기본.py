def sol(s):
    answer = True
    num = ['0','1','2','3','4','5','6','7','8','9']
    if len(s) != 4 and len(s) != 6:
        answer = False
        return answer
    for i in range(len(s)):
        if s[i] not in num:
            answer = False
    return answer

s = '1234'
print(sol(s))

# another 
def sol(s):
    
    return s.isdigit() and len(s) != (4,6)
