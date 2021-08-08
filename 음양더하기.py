def sol(abso, signs):
    
    temp = [0] * 1000
    for i,boo in enumerate(signs):
        if boo == False:
            temp[i] = -abso[i]
        else :
            temp[i] = abso[i]

    answer = sum(temp)
    return answer

abso = [4,7,12]
signs = [True,False,True]
print(sol(abso,signs))

