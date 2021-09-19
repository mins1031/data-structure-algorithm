f = int(input())
first = set(map(int,input().split()))
s = int(input())
second = list(map(int,input().split()))

for i in second:
    if i not in first:
        print("0")
    else :
        print("1")

#어떤 리스트안에 특정수가 있는지 판단할때는 리스트를 set으로 적용
#set은 중복이 없고, 순서가 뒤죽박죽임.
#파이썬은 또 not in 이라는 포함연산자도 있기에 훨씬 편하게 조회가능
#
"""
for i in range(s):
    count = 0
    for j in range(f):
        if second[i] == first[j] :
            print("1")
            break
        count += 1
    if count == 5:
        print("0")
"""
