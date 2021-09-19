import string
def sol(s):
    answer = ''
    temp = s.split(" ")
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if j % 2 == 0 :
                print('up')
                answer += temp[i][j].upper()
            elif j % 2 == 1:
                answer += temp[i][j]
        answer += ' '
    
    return answer

s = "Try hello world"
print(sol(s))

