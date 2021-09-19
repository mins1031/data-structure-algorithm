class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
            self.head = Node(data)
        else :
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next

    def delete(self,data):
        if self.head == '':
            print("노드값이 없습니다.")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else :
            while node.next:
                node = head
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else :
                    node = node.next

    def search_node(self,data):
        node = self.head
        while node.next:
            if node.data == data:
                print(node)
                return
            else :
                node = node.next
#add와 모든 내용 출력, 삭제 기능이 있는 리스트 클래스


linklist1 = NodeMgmt(0)

for i in range(1,10):
    linklist1.add(i)

linklist1.search_node(7)

"""def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
    
for i in range(2,11):
    add(i)


node3 = Node(3.5)

def insertt(index,data):
    node = head
    for i in range(index-1):
        node = node.next
        print(i)

    temp = node.next #삽입 노드의 다음 노드 주소를 temp에 저장
    node.next = data #삽입 노드 전 노드의 next값에 삽입노드 주소 저장
    data.next = temp #삽입노드의 next값에 기존 다음노드 주소 저장

insertt(3,node3)

while head.next :
    print(head.data)
    head = head.next
   """ 

"""while head.next :
    print(head.data)
    head = head.next
print(head.data)        ##리스트 중간에 값넣는 로직 구
"""



#파이썬은 클래스 변수와 인스턴스 변수가 있음.
#파이썬의 클래스는 자바와 달리 네임스페이스에 메모리가 할당되어 존재하고있음
#그래서 바로 Node.함수 이렇게 접근 가능함.
#인스턴스 변수는 클래스로 생성한 객체의 변수임. 그래서 클래스 생성자에 파라미터로
#self를 보면 self.name = "kim" 이렇게 하면 인스턴스 영역에 name = "kim"이렇게
#저장되고 클래스와는 무관함.
#위의 self.data, next도 node1,node2에 각각 생성되어있는 인스턴스 객체임
