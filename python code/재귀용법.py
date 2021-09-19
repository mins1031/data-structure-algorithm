def factorial(num):
    if num > 1 :
        return num * factorial(num-1)
    else :
        return num
#4 -> 3 -> 2 -> 1. return 1 -> return 2*1 -> return 3*2*1 ->  return 4*3*2*1

num = int(input())

print(factorial(num))

def multiple(data):
    if data <= 1:
        return data

    return data * multiple(data-1)

print(multiple(4))

def mul(data):
    sum = 1
    for i in range(1,data+1):
        sum = sum * i
    return sum
print(mul(5))
        
