length = int(input())
stack = list()

count = 1
for i in range(length):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        print("+")
    if stack[-1] == data:
        stack.pop()
        print("-")
    else :
        print("NO")
        break
#위에서 data를 입력받아 반복문으로 data수까지오름차순으로 스택에 넣어줌으로써
#스택구조를 완성하고 만약 스택의 마지막 수가 data와 일치하면 pop해줌. 이건
#만약 반복문을 거치치않고 내려온 경우는 전의 data값보다 현 data값이 작은 경우고
#작은경우pop을 하고 -출력함 이렇게 마지막 원소값을 data와 비교함으로써 내림차순
#도 확인가능

print(stack)

