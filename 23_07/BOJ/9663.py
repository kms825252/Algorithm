n = int(input())
chess = []
for _ in range(n):
    chess.append([0] * n)

cnt = 0
check = True

def check1(x, j):
    global check
    if x<=0:
        return

    if chess[x-1][j] == 1:
        check = False
        return

    check1(x-1, j)

def check2(x, j):
    global check
    if x<=0 or j<=0:
        return

    if chess[x-1][j-1] ==1:
        check = False
        return

    check2(x - 1, j - 1)

def check3(x, j):
    global check
    if x<=0 or j>=n-1:
        return

    if chess[x-1][j+1] == 1:
        check = False
        return

    check3(x-1, j +1)

def sol(x):
    global cnt
    global check

    if x == n:
        cnt += 1
        return

    for j in range(n):
        check = True
        check1(x, j)
        if check == False:
            continue
        check2(x,j)
        if check == False:
            continue
        check3(x,j)
        if check == False:
            continue

        chess[x][j] = 1
        sol(x+1)
        chess[x][j] = 0




sol(0)
print(cnt)