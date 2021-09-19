n = int(input())

s = 2
e = 7
result = 0
p = 2
i = 1
while True :
    if n == 1:
        result = 1
        break
    elif n >= s and n <= e :
        result = p
        break
    else :
        s = s + (6 * i)
        e = e + (6 * p)
        i += 1
        p += 1

print(result)

"""
수학적 규칙을 찾는 문제. 문제를 잘 안봐서 오래 고민했는데
. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다. 라는 구문이있었다.
이걸 잘 생각해보니 1을 기준으로 첫 테두리는 2, 두번쨰 테두리는 3 이어서
구간을 설정하고 입력받는 값이 구간에 해당하는지를 판단하는 로직으로 구성했다.
"""
