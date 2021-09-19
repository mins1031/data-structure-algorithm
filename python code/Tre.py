
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
        #value로 들어온 값이 현재 head로 들어온 Node객체의 값보다 작은경우
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                #만약 왼쪽의 값이 있는경우 왼쪽 객체의 주소를 기준주소로 변경하고
                #조건문 종료되 다시 반복문 타고 첫번째 if로 가서 대소비교함
                else:
                    self.current_node.left = Node(value)
                    break
                #왼쪽 값이 비어있다면 입력된 value값이 해당 주소에 저장되면됨.
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                # 만약 첫 if 조건인 root node의 값보다 큰경우라 오른쪽으로 옴
                #해서 오른쪽 값이 비어있지 않다면 오른쪽 노드객체의 주소를
                # 기준주소로 변경하고 value값의 자리를 찾을떄까지 조건 반복
                else:
                    self.current_node.right = Node(value)
                    break
                #오른쪽 값이 비어있으면 value값 넣어주고 반복문 종료!
                
            #value값을 root node부터 계속 비교해 왼,오 정하고 그쪽이 비어있으면
            #값넣고 안 비어있으면 그값을 기준노드로 바꾸고 또 비교..하고 또
            #왼,오 정하고... 이런식으로 value값의 자리를 찾는 로직을 작성해야함.

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
#이렇게에 BST라는 이진트리내에선 head값(=1)이 계속 루트 노드로 시작해 이어지는것


