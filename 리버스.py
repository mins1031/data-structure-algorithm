def sol(n):
    answer = []
    temp = list(map(int,str(n)))
    temp.reverse()
    answer = temp
    return answer

n = 12345
print(sol(n))
