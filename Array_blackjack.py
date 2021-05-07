n,m = list(map(int,input().split(' ')))
card = list(map(int,input().split(' ')))

bigcard = 0
for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            sumcard = card[i]+card[j]+card[k]
            if sumcard > bigcard and sumcard <= m :
                bigcard = sumcard

print(bigcard)
