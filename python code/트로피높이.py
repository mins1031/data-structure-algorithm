n = int(input())
heg = list()
for i in range(n):
    heg.append(int(input()))
pivot = 0
left = 0
right = 0
for i in range(n):
    if i == 0:
        pivot = heg[0]
        left += 1
    else :
        if heg[i] > pivot:
            pivot = heg[i]
            left += 1
        else :
            continue
        
for i in range(n-1,-1,-1):
    if i == n-1:
        pivot = heg[i]
        right += 1
    else :
        if heg[i] > pivot:
            pivot = heg[i]
            right += 1
        else :
            continue

print(left)
print(right)
    
            
