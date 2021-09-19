import sys

data_list = []


countcommand = int(sys.stdin.readline())

for i in range(0,countcommand):
    method = sys.stdin.readline().split()
    if method[0] == "push":
        #pushv = int(sys.stdin.readline())
        data_list.insert(0,method[1])
    elif method[0] == "pop":
        if len(data_list) == 0:
            print(-1)
        else :
            print(data_list.pop())
        
    elif method[0] == "size":
        print(len(data_list))
    elif method[0] == "empty":
        if len(data_list) == 0 :
            print(1)
        elif len(data_list) > 0 :
            print(0)
    elif method[0] == "front":
        if len(data_list) == 0:
            print(-1)
        else :  print(data_list[len(data_list) -1])
    elif method[0] == "back":
        if len(data_list) == 0:
            print(-1)
        else :
            print(data_list[0])


##front와 back의 의미가 애매했는데 그냥 front = 처음넣은 값  back = 마지막 넣은값
#이거였음...리스트의 문제 자체가 애매함 append로 추가하면 pop했을때 마지막 값이
#나오고 insert로 넣으면 잘나옴;;;; 물어보
    
