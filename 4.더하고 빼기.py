#필수 테스트 - 더하고 빼기

def digit_sub(num):
    count = 0
    value = 0
    apple = [0,9,18,27,36,45,54,63,72,81,90,99]
    pineapple = 100
    lol = 0;
    while True:
        if count == 0 :
            value = num
            count += 1
            
        target = list(map(int, str(value)))
        value = value - sum(target)
        lol += 1
        print(value)
        print(lol)
        if value < 100:
            if value % 9 == 0:
                print(value)
                return "apple"
    
            
num = 170
print(digit_sub(num))


'''
if num >= 100:
        return "apple"
    el





        if value > 100:
            return 99
        elif value <= 100:
'''
