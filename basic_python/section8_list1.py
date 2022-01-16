'''
리스트와 내장함수
'''
import random as r
# 빈 리스트 생성
a=[]
b=list()

# 일반 리스트 생성
a= [1, 2, 3, 4, 5]

b=list(range(1, 11))
#print(b)

c=a+b # 리스트 끼리 더하면 두 리스트를 합쳐준다
print(c)

a.append(6) # append는 리스트에 값추가
print(a)

a.insert(3, 7) # a리스트의 3번째에 7을 삽입한다
print(a)

a.pop() # pop은 리스트에서 마지막 수를 빼버린다
print(a)

a.pop(3) # a리스트 3번째 수를 버린다.
print(a)

a.remove(4) # a리스트에서 4라는 수를 지운다
print(a)

#a.remove(6) 값이 없으면 에러난다
#print(a)

print(a.index(5)) # a리스트의 5가 몇번째에 있는지 확인할 수 있는 index함수
a=list(range(1, 11))

print(sum(a)) # a리스트의 모든 값을 합해주는 sum함수 -> 인자의 모든 수를 합한다
print(max(a)) # a리스트의 값중 가장 큰수를 출력하는 max함수 -> 인자중 가장 큰수를 출력한다.
print(min(a)) # a리스트의 값중 가장 작은수를 출력하는 min함수 -> 인자중 가장 작은 수를 출력한다.

r.shuffle(a)
print(a)

a.sort() # a리스트를 오름차순으로 정렬해쥬는 sort함수
print(a)

a.sort(reverse=True) # sort함수 인자로 reverse를 참으로 주게 되면 내림차순으로 정렬해준다.
print(a)

a.clear() # a리스트를 비워주는 clear 함수
print(a)










