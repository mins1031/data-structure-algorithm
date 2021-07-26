# 필수 테스트 - 승점구하기

def get_point(games):
    win_point = 0
    for i in range(len(games)):
        if games[i][0] > games[i][1]:
            win_point += 3
        elif games[i][0] == games[i][1]:
            win_point += 1
        else :
            continue
    return win_point

results = [[3,4],[1,4],[4,1],[3,3],[2,1],[2,2],[2,3],[3,0],[0,0],[1,0]]
# 0 + 0 + 3 + 1 + 3 + 1 + 0 + 3 + 1 + 3 = 15
print(get_point(results))
