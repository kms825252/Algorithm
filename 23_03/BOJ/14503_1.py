import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

result = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def func(r, c, d):
    global result

    while True:
        if arr[r][c] == 0:
            result += 1
            arr[r][c] = 2


        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if arr[nr][nc] == 0:
                break

        else:
            if d == 0:
                new_r = r + 1
                if arr[new_r][c] != 1: # 벽 안쪽이라 벽 벗어나는 거 생각 안해도 될듯
                    r = new_r
                    continue
                else:
                    break
            elif d == 1:
                new_c = c - 1
                if arr[r][new_c] != 1:
                    c = new_c
                    continue
                else:
                    break
            elif d == 2:
                new_r = r - 1
                if arr[new_r][c] != 1:
                    r = new_r
                    continue
                else:
                    break
            else:
                new_c = c + 1
                if arr[r][new_c] != 1:
                    c = new_c
                    continue
                else:
                    break

        d -= 1
        if d < 0:
            d = 3
        nr = r + dr[d]
        nc = c + dc[d]

        if arr[nr][nc] == 0:
            r = nr
            c = nc
            continue

func(r,c, d)
print(result)

