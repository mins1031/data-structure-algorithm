def sol(seoul):

    target = str(seoul.index('Kim'))
    answer = "김서방은 "+target+"에 있다"
    return answer

seoul = ['jeong','min','bae','Kim','nam']
print(sol(seoul))
