import queue

data_queue = queue.Queue()
data_lifoqueue = queue.LifoQueue()

def push(data):
    data_queue.put(data)
    data_lifoqueue.put(data)

def pop():
    if data_queue.qsize() == 0 :
        print("-1")

    output = data_queue.get
    print(output)

def size():
    print(data_queue.qsize())

def empty():
    if data_queue.empty() == 1:
        print("1")
    else :
        print("0")

def front():
    if data_queue.empty() == 1:
        print(-1)
    else :
        data_queue.get_nowait()
def back():
    if data_lifoqueue.empty() == 1:
        print(data_lifoqueue.get())
    else :
        print(-1)

command = int(input())
test = push(1)
testt = push(5)
testtt = push(3)

test1 = pop()
test2 = size()
test3 = empty()
test4 = front()
test5 = back()

  for i in range(0,command) :
    ini = input()
    if ini == "push":
        pushc = int(input())
        push(pushc)
    elif ini == "front":
        front()
    elif ini == "pop":
        pop()
    elif ini == "empty":
        empty()
    elif ini == "size":
       size()
    elif ini == "back":
        back()
        
##큐는 put(),get()으로 값을 넣고뺄수있는데 문제풀이는 다 리스트로 하네..?
