n = int(input())
array = list()
for i in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]),int(input_data[1])))

array = sorted(array, key=lambda x: x[0])

print(array)
