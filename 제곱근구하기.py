import math
def sol(n):
    answer = 0
    p = math.sqrt(int(n))
    if p % 2 == 0 or p % 2 == 1:
        answer = math.pow(p+1,2)
    else :
        answer = -1
    return int(answer)

n = 121
print(sol(n))


