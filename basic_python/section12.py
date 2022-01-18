'''
람다 함수

def plus_one(x):
    return x+1


plus_two = lambda x: x+2 # 이것 자체로 함수다다. x값을 인자로 받고 x+2를 리턴해주는 함수
print(plus_two(1))
'''

# 람다는 표현식이다. 내장함수의 인자로 사용될때 유용하다고 한다
def plus_one(x):
    return x+1

a=[1, 2, 3]
print(list(map(plus_one, a)))
# 참고로 map은 첫 인자가 함수(대부분 자료형), 두번째 인자가 데이터이다.
# 데이터를 첫 인자 형으로 바꿔서 리턴해준다.

# 위처럼 하면 번거로우니
print(list(map(lambda x: x+1, a)))
# 조금 햇갈리긴 하지만 함수의 이름을 적용할 필요가 없어보이는 간단한 역할을 하는 함수를 정의할때 사용하면 좋다.
