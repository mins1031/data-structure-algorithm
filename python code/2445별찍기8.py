n = int(input())

for i in range(1,n+1):
    print("*"*i +" "*((n*2)-(i*2))+"*"*i)
for j in range(1,n):
    print("*"*(n-j)+" "*(2*j)+"*"*(n-j))
