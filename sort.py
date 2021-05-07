data = [6,4,5,19,2]

leng = len(data)

for a in range(leng-1):
    for b in range(leng-a-1):
        if data[b] > data [b+1]:
            temp = data[b+1]
            data[b+1] = data[b]
            data[b] = temp

print(data)
