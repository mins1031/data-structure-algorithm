import hashlib

s = input()
has = hashlib.sha256(s.encode())
print(has.hexdigest())

#파이썬의 sha256은 hashlib라는 클래스를 임포트 한다음 hashlib의
#sha256메서드를 통해 인코딩해주고 출력시 hexdigest()라는 메서드를 통해
#출력해주면 해슁가
