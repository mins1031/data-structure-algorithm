'''
2. 변수입력과 연산자
'''

a, b=input("숫자를 입력하세요 : ").split()
# print(type(a))  -> str 타입
c = a+b
print(type(c)) # -> str
print(c) # -> 23 출력

# 입력받은 내용을 정수로 변환하는 방법1
a = int(a)
b = int(b)
c = a + b
print(type(c)) # -> int
print(c) # -> 5

# 방법2
a, b = map(int, input("숫자를 입력하세요 : ").split())
# 두번째인자의 내용을 받아 첫번쨰 인자의 타입으로변환해 주는 함수가 map인듯 일단 정확하진 않음
print(type(a))
c = a+b
print(type(c))
print(c)

print(a+b)
print(a-b)
print(a*b)
print(a/b) # 몫을 실수화
print(a//b) # 몫 나누 
print(a%b) # 나눈 나머지
print(a**b) # 제곱 -> 6**2 6의 2제곱


a=4.3
b=5
c = a+b
print(type(c)) # 실수와 정수를 계산하면 실수가 결과 타입으로 계산
