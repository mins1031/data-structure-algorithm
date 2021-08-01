# 공통 테스트 - 숫자 더하기

def combine(num):

    sum = int((1+num) * (num/2))
    return sum

target = int(input("증가시킬 마지막수를 입력해 주세요: "))


print(combine(target))
