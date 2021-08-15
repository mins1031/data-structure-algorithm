def sol(dart):
    num = ['0','1','2','3','4','5','6','7','8','9']
    s = 'S'
    d = 'D'
    t = 'T'

    star = '*'
    acha = '#'
    temp = ''
    score = []
    for i in range(len(dart)):
        if dart[i] in num:
            temp += dart[i]
        elif dart[i] == s:
            
