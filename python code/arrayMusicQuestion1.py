list_music = list(map(int,input().split(' ')))
#문제에 입력이 1 2 3 4.. 이런식으로 한칸씩 떨어져있는 입력 예제 이기에 입력받을때
#한칸씩 떨궈서 입력받는 형식을 취해줘야해서 split(' ')이렇게 리스트를 받음.
#또한 split으로 받은 값은 ['3','5','4',..] 이렇게 문자열로 저장되기에 int를 앞에
#붙혀주어 입력값의 자료형을 명시해줌
a = 1
d = 8
m = 0;

for i in range(len(list_music)):
    if list_music[i] == a:
        a += 1
    elif list_music[i] == d:
        d -= 1

if a == 9 :
    print("ascending")
elif d == 1 :
    print("descending")
else :
    print("mixed")
