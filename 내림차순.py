def sol(num):
    answer = list(map(int,str(num)))
    answer.sort(reverse=True)
    answer = list(map(str,answer))
    
    return int(''.join(answer))

n = 12345
print(sol(n))
