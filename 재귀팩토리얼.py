def fec(data):
    if data <= 1:
        return 1
    else:
        return data * fec(data-1)
num = int(input())
print(fec(num))

"""
처음에 if문을 data == 1: retunr data로 했는데 안되서 data<= 1: return 1로 적용했
더니 통과함... 애매허네 최대한 명확하게 값을 지정해야하는듯.
"""
