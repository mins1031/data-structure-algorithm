def sol(arr):
    if len(arr) == 1:
        answer1 = [-1]
        return answer1
    answer = arr
    
    bot = min(answer)
    answer.remove(bot)
    return answer

arr = [5,8,3,9,1,2]
print(sol(arr))
