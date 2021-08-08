def sol(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    temp = [0,0,0]
    for i in range(len(answers)):

        if answers[i] == first[i%5]:
            temp[0] += 1
        if answers[i] == second[i%8]:
            temp[1] += 1
        if answers[i] == third[i%10]:
            temp[2] += 1
        

    most = max(temp)
    answer = []
    for i in range(len(temp)):
        if most == temp[i]:
            answer.append(i+1)
    
    return answer

answers = [4,3,5,1,3,5,2,4,1,2,2,4,3,1,2,3,5]

print(sol(answers))
