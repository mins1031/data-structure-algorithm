#1. print("Hello World")

#2. print("Marry\' cosmetics")
#-> Marry' cosmetic문자열 중간에 ''를 쓰려면 \를 넣어줘야 하는듯?
#2-2. print("mm\'hi\' !!")
#-> mm'hi' !!
#3. d = 3.141592
#   print("%.2f" %d)
#-> 3.14   %.4f는 3.1416인걸로 보아 .xf 는 해당하는 소수점까지 출력하고
#x자리값은 반올림하는듯
#4. 두수 입력받아 더한값 출력
#first = input()
#second = input()
#print(int(first) + int(second))
#>>6 input은 scanf,cin등과 같은 입력 함수. 출력시 int로 감싸는건 연산을 위해
#자료형을 명시해 감싸줘야 하는듯
#6. 형변환 : 문자열 '720'을 정수형으로 정수 100을 문자열 "100"으로 변환할것.
#intcv = "720" -> 파이썬에서 문자열 변수는 ""를 붙혀서 해줌.
#strcv = 100
#print(int(intcv))
#print(str(strcv))
# >>720  100  -> 이걸보며 파이썬은 변수를 선언하고 들어가는 값으로 형이 정해진다
#고 생각? 할까?
#7. 사칙연산 : 두수 입력받고 덧,뺼,곱,나눗셈 할것.
#in1 = input() >> 11
#in2 = input() >> 2
#print(int(in1) + int(in2)) >> 13
#print(int(in1) - int(in2)) >> 9
#print(int(in1) * int(in2)) >> 22
#print(int(in1) / int(in2)) >> 5.5
#print(int(in1) // int(in2)) >> 5 (몫)
#print(int(in1) % int(in2)) >> 1(나머지)  => 사칙연산자는 자바와 동일
#8. 거듭제곱 : 사용자로부터 밑과 지수를 입력 받은 후 거듭제곱 값을 출력
#in1 = input() >> 2
#in2 = input() >> 4
#print(int(in1)**int(in2)) >> 16
#9. 두 수 입력받고 나눈다음 나눈값을 1.format함수 사용해서 출력 2.소수점 첫자리만 출력
#in1 = input()
#in2 = input()
#print('{0}/{1} = {2:0.1f}'.format(in1,in2,int(in1) / int(in2)))
# format은 뭐 잘 모르겠다 잘 안쓰일거같음
#10. 기본 자료형 : 10,2.2,"hi" 각각을 변수에 넣고 각 데이터 타입 출력
#jung = 10
#sosu = 2.2
#munja = "hi"
#print(type(jung)) >> <class 'int'>
#print(type(sosu)) >> <class 'float'>
#print(type(munja)) >> <class 'str'>
# type()함수는 인자의 자료형을 반환하는 함수인듯
#11. 조건문 : 두수 입력 받아 큰수를 화면에 출력
#in1 = input()
#in2 = input()
#if in1 > in2:
#    print(in1)
#else :
#    print(in2)
#파이썬은 포문이든 if문이든{} 대신 : 를 사용해 문들을 개괄해줌.
#12. 조건문 : 입력받은 수가 홀인지 짝인지 출력
#in1 = int(input())
#if in1 % 2 == 0:
 #   print("짝수")
#else :
#    print("홀수")
#비교연산자중 동일연산자는 ==로 자바와 동일
#13. 조건문 : 세게의 수를 받고 가장 작은수를 출력
#in1 = int(input())
#in2 = int(input())
#in3 = int(input())
#if in1 < in2 :
#    min = in1
#else :
#    min = in2
#if min < in3 :
#    print(min)
#else :
#    print(in3)
# else에는 조건이 못들어가나보다.. 충격적임.=> else조건은 elif로 써줘야함
# 14. 조건문 : 점수를입력 받고 등급 출력
#in1 = int(input())
#if  in1 >= 81 :
#    print("A")
#elif 80 >= in1 >= 61:
#    print("B")
#elif in1 <= 60:
#    print("C")
# 위처럼 해도 되지만 &대신 and로 사용하는듯?해서 80 >= in1 and 61 <= in1 이렇게도 가능
# 15. 데이터 구조(리스트): 주민번호를 입력받아 출새년도 출력
#num = input()
#print(num[1:3]+ "년생")
#num[x:y] x는 시작점 y는 끝점이어서 시작값 부터 끝값 전까지 값들을 출력함
#961014[4:5] => 1, [1:3] => 61, [0:2] => 96 [2] => 1
#16. 문자열 다루기(strip) : 다음문자열에서 ...을 제거
#in1 = "a man...and woman..."
#print(in1.strip("..."))
# 애매함 중간에 ...은 안없어짐 중간 값은 못없애고 문자열 앞뒤로 있는 값을 없애는듯
# 17. 문자열 다루기count  : 문자열에서 특정 문자열 빈도수
#in1 = "hi is a name. name is you. you is back!"
#count = in1.count("name")
#print(count) >> "2"
#좋은듯? 이걸로 크롤링하는듯하다.
#18. 문자열 다루기(인덱싱) : 문자열에서 두번째,네번째 문자 출력
#letter = "minyoung"
#print(letter[1]) >> i
#print(letter[3]) >> y
#배열처럼 써주면 되는듯?
#19. 문자열 다루기(split) : letter변수에 문자열중 ,를 기준으로 분리해 출력
#letter = "Dave, janet, min, andy"
#letter_list = letter.split(",")
#print(letter_list)
#for letter in letter_list:
#    print(letter)
#split()인자값을 기준으로 배열을 만드는듯?
#20. 반복문 : 1~10 더한 값 출력
#sum = 0
#for num in range(1,11):
#    sum += num
#print(sum)
#num2= 1
#total=0
#while num2 < 11:  
#    total += num2
#    num2 += 1
#print(total)
#for문과while문 사용법 +=연산도 파이썬에서 자바와 동일하게 가능
#strings = input()
#for string in strings.split(","):
#    print(string)
#for문 과 split사용법 
#list_data= ["hi min","hi janet","how are you today?","i am good!"]
#for data in list_data:
#    print(data+"is length",len(data))
#>> hi minis length 6 이런식으로 print문에서 ,하면...애매하네 암튼 길이도 구할
#data =[1,2,3,4,5,6,7,8,9,10]
#data.reverse()
#for num in data:
#    print(num)
#reverse()라는 함수로 구성물을 반대로 역전시킬수 있는듯?
#25. 리스트중 txt파일 출력
#filelist = ['exercise01.docx','exercise02.csv','exercise03.txt']
#for filename in filelist:
#    if filename.split(".")[1] == "txt":
#        print(filename)
#아마 split(".")[1]은 split으로 .을기준으로 첫 리스트값이 둘로 나눠짐. 이렇게
#나눠지는 값을 배열에 담는 원리때문에 [1]을하면 .뒤의 파일형식을 알수 있는듯
##!!! 파이썬에서 튜플은  ()해당 괄호로 구현하고 정수,문자열등 일반적인 자료형 뿐
#만 아니라 함수,딕셔너리,리스트등 다넣을수 있음. 다만 해당값을 수정하거나 추가할
#수 없음 
