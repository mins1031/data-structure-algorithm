'''
3. 조건문 if(분기, 중첩)
'''

x=7
if x==7:
    print("Lucky") # 7과 x가 같으면 동작

x=5
if x!=7:    
    print("!=") # x가 7이 아니면 동작

x=15
if x>=10:
    if x%2==1:
        print("10이상의 홀수")

if x>= 10 and x%2==1:
    print("10이상의 홀수")


x=10
if x>0:
    print("양수")
else:
    print("음수")

x=87
if x>=90:
    print("a")
elif x>=80:
    print("b")
elif x>=70:
    print("c")
else:
    print("d")
