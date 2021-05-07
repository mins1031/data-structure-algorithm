def hmoon(voc):
    if len(voc) == 1:
        return True
    
    if voc[0] == voc[-1]:
        return hmoon(voc[1:-1])
    else :
        return False
    
voc1 = str(input())
a = list(voc1)
print(a)
b = hmoon(voc1)
print(b)
