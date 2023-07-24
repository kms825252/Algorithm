n = int(input())
chess = []
for _ in range(n):
    chess.append([0] * n)

cnt = 0

def sol():
    global cnt
    if 1 in chess[-1]:
        cnt += 1
        return

    for i in range(n):
        for j in range(n):
            if 1 in chess[i]:
                continue
            if 1 in chess[i][j]:
            chess[i][j] = 1
            sol()