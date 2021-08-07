def solution(price, money, count):

    answer = 0;
    total = 0;

    for i in range(count+1):
        total += price * i

    if total > money:
        answer = total - money
        
    return answer

price = 3
money = 20
count = 4

print(solution(price,money,count))
