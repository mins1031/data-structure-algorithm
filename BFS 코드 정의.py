def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    
    need_visit.append(start_node)
#이렇게 방문했던 노드 큐, 방문해야할 노드 큐, 시작 노드 값을 설정하고 시작함.    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph,'A'))

"""
1) need_visit큐는 방문해야할 노드를 담는 큐 , visited큐는 방문했던 노드를 담는 큐임
2) 처음 인접노드를 저장했던 딕셔너리의 시작값을 n큐에 넣어주는 것을 시작으로 함.(키값)
3) 이후 n큐의 맨앞데이터를 꺼냄. 그 값이 v큐에 있는지 확인해봄.
4) 없으면 꺼낸 데이터를 v큐에 넣고 그 키값데이터의 벨류 데이터를 n큐에 넣음.
5) 다음으로 또 n큐에서 하나를 꺼내서 v큐에 키값이 있는지 확인.
6) 없다면 v큐에 꺼낸 키값을 넣어주고, 기존 n큐값 뒤에 v큐에 들어간 키값의 벨류값들을
넣어줌
7) 반복하다 v큐에서 값을꺼내 n값에 있는지 확인했는데 있을경우 아무것도 안하고 
다음으로 넘어감.
8) 이렇게 모든 노드의 값을 bfs = 너비우선 탐색 방식으로 탐색이 가능하다.
+++ bfs의 시간복잡도는 특이하게도 노드갯수(V)와 간선갯수(E)의 합 만큼 반복문이
동작하기 때문에 시간복잡도는 O(V+E) 이다.
간선갯수는 노드갯수 -1로 보는게 맞을듯.
"""
