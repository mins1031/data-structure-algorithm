def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))

"""
if에 n <=2로만 해서 틀렸었음.. 모든 기본조건 다 걸어줘야 맟혀줌ㅋ"""
