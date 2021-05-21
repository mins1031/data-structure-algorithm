t = int(input())
data = [1,2,4]
for i in range(3,10):
    data.append(data[i-1] + data[i-2] + data[i-3])

for i in range(t):
    num = int(input())
    print(data[num-1])

"""
t = int(input())
def sumsum(target):
    data = [0 for i in range(target)]
    data[0] = 1
    data[1] = 2
    data[2] = 4
    
    if target == 1:
        return 1
    elif target == 2:
        return 2
    elif target == 3:
        return 4
    else :
        for i in range(3,target):
            data[i] = data[i-1] + data[i-2] + data[i-3]

    return data[target-1]

for i in range(t):
    num = int(input())
    print(sumsum(num))
"""
#위의 내용은 값은 잘 나오는데 인덱스에러가나옴...인덱스 부분이 잘못된듯
#DP의 기본적인 문제풀이임. 점화식은 써놓고 내가 못구하는 게 많지만 익숙해지면
#여러방면으로 잘 예상해볼거같긴하다.
