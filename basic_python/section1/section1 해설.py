'''
변수명 정하기
1) 영문과 숫자, _ 로 이루어 진다
2) 대소문자를 구분한다
3) 문자나 _로 시작한다
4) 특수문자를 사용하면 안된다 (&, %) 등
5) 키워드를 사용하면 안된다. (if, for등)
'''
a = 1
print(a)

#값 교환
a, b= 10,20
print(a, b) # 10 ,20
a, b = b, a
print(a, b) # 20, 10

#변수 타입
a=12345
print(type(a)) # type 함수는 인자의 타입을 출력해준다. -> <class 'int'>
a=12.1232141515
print(type(a)) # 참고로 float은 8바이트까지의 값 밖에 출력되지 않음
a = 'student'
print(type(a)) 

#출력방식
print('number')
a, b, c=1 ,2 ,3
print(a, b, c) # -> 1 2 3
print(a,b,c, sep=', ') #sep은 출력되는 값들 사이에 값을 넣어주는 역할을 해준다 -> 1, 2, 3
print(a,b,c, sep='\n')
print(a, end=" ") # end는 print후 줄바꿈이 기본값인데 줄바꿈말고 다른 작업을 해주는 경우 적용한다./
