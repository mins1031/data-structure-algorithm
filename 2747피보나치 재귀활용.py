"""def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibo(num-1) + fibo(num-2)


print(fibo(int(input())))
#백준 문제에선 시간초과남. 재귀용법의 한계를 보여주는 대표적 문제임.
#동적 계획법(다이나믹 프로그래밍)으로 구현해야함.
"""
#동적계획법
def fibo(num):
    cache = [0 for i in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2,num+1):
        cache[index] = cache[index-1] + cache[index-2]

    return cache[num]
    
print(fibo(int(input())))
