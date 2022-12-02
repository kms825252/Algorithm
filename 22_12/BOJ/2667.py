from pprint import pprint
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
def dfs(x,y):
    global cnt
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    if arr[x][y] ==1:
        cnt += 1
        arr[x][y] = 2
        for j in range(4):
            ni = x + di[j]
            nj = y + dj[j]

            if 0 <= ni < n and 0 <= nj < n :
                dfs(ni,nj)

ans = []
for k in range(n):
    for l in range(n):
        if arr[k][l] == 1:
            cnt = 0
            dfs(k,l)
            if cnt >= 1:
                ans.append(cnt)

ans.sort()
print(len(ans))
for m in ans:
    print(m)