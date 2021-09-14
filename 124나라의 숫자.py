def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        print(n)
        answer = '124'[n%3] + answer
        n //= 3
        print(n)
        print(answer)
    return answer

n = 10
print(solution(n))
