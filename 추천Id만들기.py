def sol(new_id):
    answer = ''
    id_list = list(new_id)
    permit = ['0','1','2','3','4','5','6','7','8','9','-','_','.']
    count = 0
    for i in range(len(id_list)):
        if id_list[i].isupper():
            id_list[i] = id_list[i].lower()

    while True:
        if count >= len(id_list):
            break
        
        if id_list[count] not in permit and not id_list[count].isalpha():
            del id_list[count]
            continue
        count += 1

    count = 0
    while True:
        if count >= len(id_list):
            break
        
        if count != len(id_list) - 1:
            if id_list[count] == '.' and id_list[count+1] == '.':
                del id_list[count]
                print('h')
                continue
        count += 1
    for i in range(len(id_list)):
        if id_list[0] == '.':
            del id_list[0]
        if len(id_list) == 0 :
            break
        if id_list[-1] == '.':
            del id_list[-1]
        if id_list[0] != '.' and id_list[-1] != '.':
            break
        
    if len(id_list) == 0:
        id_list.append('a')
    if len(id_list) >= 16:
        id_list = id_list[0:15]
        if id_list[-1] == '.':
            del id_list[-1]
    if len(id_list) <= 2:
        if len(id_list) == 1:
            id_list.append(id_list[0])
            id_list.append(id_list[0])
        if len(id_list) == 2:
            id_list.append(id_list[1])

    answer = ''.join(id_list)
    return  answer

#new_id = '...!@BaT#*..y.abcdefghijklm'
new_id = "123_.def"
print(sol(new_id))




    
