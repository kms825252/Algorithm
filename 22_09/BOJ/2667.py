def dfs(x,y):
    global cnt
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    stack = []
    stack.append((x,y))
    while stack:
        x,y = stack.pop()
        arr[x][y] = cnt
        check[cnt] += 1
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0<= ni < n and 0 <= nj < n:
                if arr[ni][nj] == '1':
                    stack.append


n = int(input())
arr = [list(input()) for _ in range(n)]
check = [0] * (n*n//2 + 1)
cnt = 0
for k in range(n):
    for l in range(n):
        if arr[k][l] == '1':
            cnt +=1
            dfs(k,l)

print(cnt, arr, check)
