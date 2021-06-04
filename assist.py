e = input()
word = []
word = e.split(" ")
print(len(word))
print(word)
dic = dict()

for i in range(len(word)):
    dic.setdefault(word[i])
    count = 0
    for j in range(len(word)):
        same = 0
        if word[j] == word[i]:
            if same != 0:
                continue
            count += 1
            same += 1 
    
    dic[word[i]] = int(count)

print(dic)


