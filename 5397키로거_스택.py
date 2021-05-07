testcase = int(input())
resultlist = list()
for j in range(testcase) :
    keylogger = list(input())
    length = len(keylogger)
    pwd = list()

    cursor = 0

    for i in range(len(keylogger)) :
        if keylogger[i] == '<' :
            if cursor == 0:
                continue
            cursor -= 1
        elif keylogger[i] == '>' :
            if cursor == len(pwd) :
                continue
            cursor += 1
        elif keylogger[i] == '-' :
            pwd.pop()
            cursor -= 1
        else :
            pwd.insert(cursor,keylogger[i])
            cursor += 1
    resultlist.append(pwd)
    
print(''.join(resultlist))
"""
test_case = int(input())
for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
"""
