n,m = map(int,input().split())
data = list(map(int,input().split(' ')))
pivot = 0;

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            hap = data[i]+data[j]+data[k]
            if m < hap:
                continue
            elif m >= hap:
                if hap > pivot:
                    pivot = hap
                else :
                    continue

print(pivot)
