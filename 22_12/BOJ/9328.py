from pprint import pprint

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def f(x,y):
    if case[x][y] == '.':
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]

            if 0 <= ni < row and 0 <= nj < col:
                f(ni, nj)



t = int(input())
for _ in range(t):
    row, col = map(int, input().split())
    case = []
    for _ in range(row):
        case.append(list(input()))
    door_key = list(input())

