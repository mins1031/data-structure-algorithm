def sol(n):

    temp = list(map(int,str(n)))
    answer = sum(temp)
    return answer

n = 123
print(sol(n))

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)
#먼저 숫자가 10이하면 1의 자리 수밖에 없기에 바로 리턴해주고
#재귀구조를 통해 10으로 나눠 자릿수 마다 더해서 리턴한다.;
