import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def func(r, c, d):
    global result

    if arr[r][c] == 0:
        result += 1
        arr[r][c] == 2

    for i in range(4):
        d -= 1
        if d < 0:
            d = 3
        nr = r + dx[d]
        nc = c + dy[d]

        if arr[nr][nc] == 0:
            func(nr, nc, d)
    else:
        if d == 0:
            new_r = r + 1
            if arr[new_r][c] != 1: # 벽 안쪽이라 벽 벗어나는 거 생각 안해도 될듯
                func(new_r, c, d)
            else:
                return result
        elif d == 1:
            new_c = c - 1
            if arr[r][new_c] != 1:
                func(r, new_c, d)
            else:
                return result
        elif d == 2:
            new_r = r - 1
            if arr[new_r][c] != 1:
                func(new_r, c, d)
            else:
                return result
        else:
            new_c = c + 1
            if arr[r][new_c] != 1:
                func(r, new_c, d)
            else:
                return result

func(r,c, d)
print(result)

