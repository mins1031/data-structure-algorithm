#우선 root node, node.right,left,value , current_node , temp_node(주소값 바꿀때
#임시저장 주소)
#힙의 정책 1) 루트 노드로부터 왼쪽값부터 채워넣어져야함
#2) 부모노드는 자식노드보다 크거나 같아야함(최대값 힙인 경우) 최소값힙은
#반대로 부모노드가 자식노드보다 작거나 같아야함

class Heap:
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_on(self,insert_idx):

        if insert_idx <= 1:
            return False

        parent_idx = insert_idx // 2
        if self.heap_array[parent_idx] < self.heap_array[insert_idx] :
            return True
        else :
            return False

    def move_down(self,pop_idx):
        if len(self.heap_array) <= 1:
            return False

        left_child_poped_idx = pop_idx * 2
        right_child_poped_idx = pop_idx * 2 + 1

        if left_child_poped_idx >= len(self.heap_array):
            return False
        elif right_child_poped_idx >= len(self.heap_array):
            if self.heap_array[right_child_poped_idx] > self.heap_array[pop_idx]:
                return True
            else :
                return False
        else :
            if self.heap_array[right_child_poped_idx] > self.heap_array[left_child_poped_idx]:
                if self.heap_array[right_child_poped_idx] > self.heap_array[pop_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[pop_idx]:
                    return True
                else:
                    return False
                    
    def insert(self,data):
        if len(self.heap_array) == 0:
            self.heap_array = list()
            self.heap_array.append(None)
            self.heap_array.append(data)

        self.heap_array.append(data)

        insert_idx = len(self.heap_array) -1

        while self.move_on(insert_idx):
            parent_idx = insert_idx // 2
            self.heap_array[parent_idx],self.heap_array[insert_idx] = self.heap_array[insert_idx],self.heap_array[parent_idx]
            insert_idx = parent_idx

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        return_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        pop_idx = 1

        while self.move_down(pop_idx):
            left_child_pop_idx = pop_idx * 2
            right_child_pop_idx = pop_idx * 2 + 1

            if right_child_pop_idx >= len(self.heap_array):
                if self.heap_array[right_child_pop_idx] > self.heap_array[pop_idx]:
                    self.heap_array[left_child_pop_idx],self.heap_array[pop_idx] = self.heap_array[pop_idx] , self.heap_array[right_child_pop_idx]
                    pop_idx = left_child_pop_idx
            else :
                if self.heap_array[right_child_pop_idx] > self.heap_array[left_child_pop_idx]:
                    if self.heap_array[right_child_pop_idx] > self.heap_array[pop_idx]:
                        self.heap_array[right_child_pop_idx], self.heap_array[pop_idx] = self.heap_array[pop_idx], self.heap_array[right_child_pop_idx]
                        pop_idx = right_child_pop_idx
                else :
                    if self.heap_array[left_child_pop_idx] > self.heap_array[pop_idx]:
                        self.heap_array[left_child_pop_idx], self.heap_array[pop_idx] = self.heap_array[pop_idx], self.heap_array[left_child_pop_idx]
                        pop_idx = left_child_pop_idx

        return return_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
