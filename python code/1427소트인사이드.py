"""
n = int(input())
array = list()

for i in str(n):
    array.append(i)

array.sort()
array.reverse()
print("".join(array))

"""
#=> 다른 풀이
array = input()

for i in range(9,-1,-1):
    for j in array:
        if int(j) == i:
            print(i,end='')



#이문제는 거의 구글링으로 함수 알아내서 풀었다고 해도 과언이아님
#1) str은 괄호안의 값을 문자열로 변환하는데 이떄 문자열은 배열처럼
#인덱스를 통해서 나눠?줄수 있는듯 해서 문자열의 자리수가 나눠질수 있었다고 생각
#=> 2134 입력받고 print(str(n)[0])처럼 조작하면 2가 출력됨!
#2) sort()는 오름차순 정렬, reverse()는 내림차순 정렬 함수!
#3) "".join(리스트이름)는 리스트의 내용물들을 ""를 중간에두고 합쳐줌
#ex) array = ["1996","10","14"] print("-".join(array)) => 1996-10-14
#+++++
#array = input()로 2134문자열로 받고 print(array[0])->2 print(array[2])->3
#출력됨 멍청하게 str로 바꿀 필요가 없었음...

##다른풀이 파트는 개지림 9부터 0까지 수가 리스트 자리수와 비교해 일치하면
#줄바꿈안하고 출력함 ex) 769985 => 998765 이렇게 나옴.;;
