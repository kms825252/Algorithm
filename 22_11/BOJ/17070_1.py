import sys

n = int(sys.stdin.readline())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

garo = 0
sero = 1
dae = 2
cnt = 0

def dfs(i, j, t):
    global cnt
    if (i, j) == (n-1,n-1):
        cnt += 1
        return

    if t == garo or t == dae:
        if j+1 < n and case[i][j+1] == 0 :
            dfs(i, j+1, garo)

    if t == sero or t == dae:
        if i +1 <n and case[i+1][j] ==0:
            dfs(i+1, j, sero)

    if i+1<n and j+1 < n :
        if case[i+1][j] == 0 and case[i][j+1] == 0 and case[i+1][j+1] == 0:
            dfs(i+1, j+1, dae)

dfs(0, 1, garo)
print(cnt)