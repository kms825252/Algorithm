
board = []

for _ in range(9):
    board.append(list(map(int, input().split())))

def check1(i, j):
    if board[i].count(0) == 1:
        num = 45
        board[i][j] = num - sum(board[i])

def check2(i, j):
    num = 45
    cnt = 0
    for k in range(9):
        if board[k][j] == 0:
            cnt += 1
        num -= board[k][j]
        if cnt > 1:
            break
    else:
        board[i][j] = num

def check3(i, j):
    num = 45
    cnt = 0
    r = i//3
    c = j//3
    for k in range(r,r+3):
        for l in range(c, c+3):
            if board[k][l] == 0:
                cnt += 1
            num -= board[k][l]

    if cnt == 1:
        board[i][j] = num

def sol(board):
    blank = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blank.append([i, j])


    while blank:
        for i,j in blank:
            check1(i, j)
            if board[i][j] != 0:
                blank.remove([i,j])
                continue
            check2(i, j)
            if board[i][j] != 0:
                blank.remove([i,j])
                continue
            check3(i, j)
            if board[i][j] != 0:
                blank.remove([i,j])
                continue


sol(board)
print(board)