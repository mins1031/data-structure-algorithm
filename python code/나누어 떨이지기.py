def sol(arr,div):
    answer = []
    for i in arr:
        if i % div == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

arr = [1,3,5,3]
div = 2
print(sol(arr,div))
