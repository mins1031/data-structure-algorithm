'''
함수 만들기


def add(a, b):
    c=a+b
    print(c)

add(3, 2)

--- 일반 함수 생성 및 동작

def add(a, b):
    c=a+b
    return c

result = add(3, 2)
print(result)
print(add(5, 7))

--- 함수 리턴 및 활용

def add(a, b):
    c=a+b
    d=a-b
    return c, d # 튜플로 리턴된다.
print(add(5,3))

--- 함수에서 다중 인자 리턴시 튜플 타입으로 리턴된다.

'''

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13 ,7 ,9, 19]
for i in a:
    if isPrime(i):
        print(i)



