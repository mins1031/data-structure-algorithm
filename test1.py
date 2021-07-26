#분기 숫자 구하기

import math

def distinction_quarter(month) :
    quarter = math.ceil(month / 3.0)
    return quarter

while True:
    month = int(input("분기를 파악할 달을 1~12사이 수로 입력해주세요 : "))
    if month < 1 or month > 12:
        print("1~12 사이의 수만 입력해주세요")
    else :
        break
       
print(distinction_quarter(month))

