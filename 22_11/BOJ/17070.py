di = [0, 1, 1]
dj = [1, 1, 0]
cnt = 0

def f(x,y):
    global cnt
    global case
    if x == n-1 and y == n-1:
        cnt +=1
        print(case)
        case = case1[:]
    if case[x][y] ==2:

        if case[x][y-1] == 2:
            for i in range(2):
                ni = x + di[i]
                nj = y + dj[i]
                if i == 1:
                    if ni < n and nj < n and case[ni][nj] != 1 and case[ni-1][nj] != 1 and case[ni][nj-1] != 1:
                        case[ni][nj] = 2
                        f(ni, nj)
                else:
                    if ni < n and nj < n and case[ni][nj] != 1:
                        case[ni][nj] = 2
                        f(ni, nj)

        elif case[x-1][y] == 2:
            for i in range(2):
                ni = x + di[i+1]
                nj = y + dj[i+1]
                if i == 1:
                    if ni < n and nj < n and case[ni][nj] != 1 and case[ni - 1][nj] != 1 and case[ni][nj - 1] != 1:
                        case[ni][nj] = 2

                        f(ni, nj)
                else:
                    if ni < n and nj < n and case[ni][nj] != 1:
                        case[ni][nj] = 2
                        f(ni, nj)

        elif case[x-1][y-1] == 2:
            for i in range(3):
                ni = x + di[i]
                nj = y + dj[i]
                if i == 1:
                    if ni < n and nj < n and case[ni][nj] != 1 and case[ni - 1][nj] != 1 and case[ni][nj - 1] != 1:
                        case[ni][nj] = 2
                        f(ni, nj)
                else:
                    if ni < n and nj < n and case[ni][nj] != 1:
                        case[ni][nj] = 2

                        f(ni, nj)


n = int(input())
case1 = [list(map(int,input().split())) for _ in range(n)]
case = case1[:]
print(case)

case[0][0] = 2
case[0][1] = 2

f(0,1)
print(cnt)



