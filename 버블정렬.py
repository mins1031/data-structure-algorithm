s = [4,2,7,5,44,37]

for j in range(len(s)):
    swap = False
    for i in range(len(s) - j):
        if i == len(s)-1:
            continue
        if s[i] > s[i+1]:
            s[i],s[i+1] = s[i+1],s[i]
            swap = True
    if swap == False:
        break

print(s)
   

