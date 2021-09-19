num= int(input())
data = [9,17]

p = 2

for i in range(2,num+1):
    data.append(i + (p*7 ) + (i-1))
    p = p**i

print(data[num])
