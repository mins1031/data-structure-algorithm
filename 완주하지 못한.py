def sol(part,comp):
    answer = ""
    for i,man in enumerate(part):
        if man not in comp:
            answer = man
        elif part.count(man) > 1:
            answer = man
            break
        
    return answer

part = ["leo", "kiki", "eden"]
comp = ["eden", "kiki"]
#print(sol(part,comp))
a = 'pol'
b = 'pol'
test = []
test.append(a)
test.append(b)

print(hash(test[0]))
print(hash(test[1]))
