n = int(input())

s = 1
count = 0
while n != 0:
    if k > n:
        k = 1
    n -= k
    k += 1
    count += 1
print(count)
