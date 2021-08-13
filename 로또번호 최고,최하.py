def sol(lottos,wins):
    rate = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    same_count = 0
    zero_count = 0
    for i,num in enumerate(lottos):
        if num in wins:
            same_count += 1
        if num == 0 :
            zero_count += 1

    best = same_count + zero_count
    answer = []
    answer.append(rate[best])
    answer.append(rate[same_count])
    answer.sort()
    return answer

lottos = [45,4,35,20,3,9]
wins = [20,9,3,45,4,35]
print(sol(lottos,wins))
