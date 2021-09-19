c,r = input().split()
c = int(c)
r = int(r)
board = [[0 for i in range(int(c))] for j in range(int(r))]
count = 0
for i in range(c):
    board[i] = list(map(str,input().split()))

print(board)
for i in range(c):
    for j in range(r):
        if i == j:
            if board[i][j] != '.':
                count += 1
print(count)
