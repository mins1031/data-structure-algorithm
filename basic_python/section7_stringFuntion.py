'''
문자열과 내장 함수
'''
msg="It is Time"
print(msg.upper())
# upper함수는 msg의 내용을 모두 대문자로 적용시킴. 다만 msg의 값이 대문자로 바뀌는건 아님
print(msg.lower()) # lower함수는 msg의 내용을 모두 소문자로 적용시킴. ''
print(msg)
tmp=msg.upper()
print(tmp)
print(tmp.find('T')) # find함수는 인자의 내용이 문자열 몇번쨰에 포함되어있는지 출력해준다.

print(msg[:2]) # msg의 0,1번째 까지, 2번 전까지 슬라이싱해서 출력해준다.
msgSlice = msg[:4]
print(msgSlice)
print(msg[3:5]) # 3번째 부터 4번째 까지 출력
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end="")
print("")
for i in msg: # 이렇게 구현하면 msg하나하나 반복문이 돌게되어서 문자열 하나씩 출력된다.
    print(i, end=' ')
print()
for i in msg:
    if i.isupper(): # 문자가 대문자인지를 참,거짓으로 검증하는 함수
        print("up",i)
    if i.islower(): # 문자가 문자인지를 참,거짓으로 검증하는 함수
        print("low", i)
for i in msg:
    if i.isalpha(): # 알바펫인지 아닌지 검증하는 함수
        print(i, end=' ')
print()

tmp = "AZ"
for x in tmp:
    print(ord(x)) # ord는 아스키코드를 출력해준다.

tmp = "az"
for x in tmp:
    print(ord(x)) # ord는 아스키코드를 출력해준다.

tmp =65
print(chr(tmp)) # chr은 숫자를 알맞는 아스키코드 문자로 출력해준다.
