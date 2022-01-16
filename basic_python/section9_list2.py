'''
리스트와 내장함수 2
'''
a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a)) # 리스트의 길이를 구하는 len함수

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

for x in enumerate(a): # enumerate는 리스트 내용을 인덱스와 값 형태의 튜플로 출력해준다.
    print(x)


# 튜플이란? 리스트와 거의 동일하지만 다른점은 튜플은 값을 변경할수 없다는 차이점이 있다.
# 자바의 배열과 같은 느낌
b=(1, 2, 3, 4, 5) # 
print(b[0])
print(b)

# 튜플 반복문과 사용 방식
for x in enumerate(a):
    print(x[0], x[1])

print()
for index, value in enumerate(a):
    print(index, value)

# all함수는 괄호내의 내용이 참이면 참을 리턴, 거짓이면 거짓을 리턴하는데
# 밑 예처럼 특정 리스트의 반복을 돌면서 리스트중 하나라도 조건을 만족 못하면 false리턴, 모두 만족하면 true리턴한다

if all(50>x for x in a):
    print("yes")
else :
    print("no")

# any 함수는 괄호내 조건이 한번이라도 참이라면 true리턴, 모두 거짓이라면 false를 리턴한
if any(5>x for x in a):
    print("yes")
else :
    print("no")

    
