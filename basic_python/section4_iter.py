'''
4. 반복문
'''
a=range(1,11) # range는 해당하는 숫자까지 정수리스트를 만들어주는 함수이다. 
print(list(a))

for i in range(1,11):
    print(i)
    print(type(i))

for i in range(10,0,-1):
    print(i)
# range를 큰수에서 작은수로 리스트만들땐 인자 2개로 해선 안되고 각 연산마다
#규칙에 해당 하는 인자를 하나 더 사용하는 즉 인자를 3개사용하는 range함수를 사용해야한다

#만약 큰수 -> 작은수가 아니더라도 1~11까지 2씩 증가 시키고 싶다면 아래처럼 구현한
for i in range(1,11,2):
    print(i)

print('=========while=======')
i=1
while i<=10:
    print(i)
    i=i+1
    
print('=========while=======')

i=10
while i>=1:
    print(i)
    i=i-1

#for-else구문: 이건 처음봐서 신기했다. for문이 자신의 할당만큼, 즉 정상적으로 할당된 양을 반복하고
#종료된경우 실행된다. 만약 중간에 break같은 부분으로 할당된 반복을 다 하지 못하고 종료된 경우는실행되지 않는다.   
for i in range(1,11):
    print(i)
else:
    print("for-else")
print("======break=======")
for i in range(1,11):
    print(i)
    if i == 5 :
        break
else:
    print("for-else") # else실행 x
