def sol(numbers,hand):
    answer = ''
    pad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    l_pad = ['1','4','7']
    r_pad = ['3','6','9']
    m_pad = ['2','5','8']
    z_pad = ['0']
    
    l_point = '*'
    r_point = '#'
    distance = 0
    for i in numbers:
        if i in l_pad:
            answer += 'L'
        elif i in r_pad:
            answer == 'R'
        elif i in m_pad:
            if i > l_point:
                
            
    return answer

nums = [1,3,4,5,8,2,1,4,5,9,5]
pad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
print(pad.index('*'))
