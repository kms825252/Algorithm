def dfs(x,y):
    case[x][y] = 0


N, M = map(int, input().split())
case = [list(map(int, input().split())) for _ in range(N)]
