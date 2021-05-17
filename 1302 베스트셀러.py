n = int(input())
t = 0
name = ""
dic = {}
for i in range(n):
    book = input()
    if book not in dic:
        dic[book] = 1
    else :
        dic[book] += 1
        
pivot = max(dic.values())
array = []
for book,number in dic.items():
    if number == pivot:
        array.append(book)
        
print(sorted(array)[0])
