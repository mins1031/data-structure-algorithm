'''
문자열과 내장 함수
'''
msg="It is Time"
print(msg.upper()) # upper함수는 msg의 내용을 모두 대문자로 적용시킴. 다만 msg의 값이 대문자로 바뀌는건 아님
print(msg.lower()) # lower함수는 msg의 내용을 모두 소문자로 적용시킴. ''
print(msg)
tmp=msg.upper()
print(tmp)
print(tmp.find('T')) # find함수는 인자의 내용이 문자열 몇번쨰에 포함되어있는지 출력해준다.

