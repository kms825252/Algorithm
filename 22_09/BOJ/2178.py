from collections import deque

def bfs(x,y):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1 ,0]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]

            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1:
                    queue.append((ni,nj))
                    arr[ni][nj] = arr[x][y] + 1

    return arr[n-1][m-1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

print(bfs(0,0))