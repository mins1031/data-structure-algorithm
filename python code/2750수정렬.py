n = int(input())
give = list()


for i in range(n):
    inp = int(input())
    give.append(inp)
"""
for i in range(n-1):
    lowest = i
    for j in range(i+1,n):
        if give[lowest] > give[j]:
            lowest = j
    give[lowest], give[i] = give[i], give[lowest]

for i in range(n):
    print(give[i])
"""
give.sort()

for i in range(n):
    print(give[i])
