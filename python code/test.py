num = int(input('7~9자리 정수를 입력해라: '))
list = []
"""
for i in range(len(str(num))):
    list.append(num[i])
print(list)

leng = len(num)
print(leng)
list.reverse()
check = 0
for i in range(0,leng+1):
    print(check)
    if i == 0 or check ==0:
        check += 1
        continue;
    if check % int(3) == 0:
        print("3의 배수!!")
        check = 0
        list.insert(i,'.')
        continue;
    check += 1

print(list)
list.reverse()
print(''.join(list))

while True:
    leng = len(num)
    list.reverse()
    for i in range(leng,0):
        if i % 3 == 0:
            list[i].insert(".")
    """
s = "%d" % num

print(s[-3])

s = '1234567'
p = []
p.append(s[-3:])
s=s[:-3]
s=s+','.join(p)
print(p)
print(s)
p.reverse()
print(p)
 
