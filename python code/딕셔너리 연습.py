graph = dict()
graph['1'] = ['B', 'C']
graph['2'] = ['A', 'D']
"""graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
"""
print(graph)

#graph['A'].append('P')
#print(graph)
n = input()

graph[n].append('L')
print(graph)
