def sol(d,bud):
    answer = 0
    d.sort()
    col = 0
    count = 0
    for i in range(len(d)):
        if col + d[i] > bud:
            break
        
        col += d[i]
        count += 1
        print(count)
    answer = 
    return answer

d = [2,2,3,3]
bud = 10
print(sol(d,bud))
