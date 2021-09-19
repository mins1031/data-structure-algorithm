def ppp(num):
    print(num)
    if num == 1:
        #print(num)
        return num
    
    if num % 2 == 1:
        #print(3*num+1)
        return (ppp(3 * num +1))
    else :
        #print(num // 2)
        return (ppp(num // 2))

n = int(input())
ppp(n)
