n = int(input())
cnt = 0
row = [0] * n

def check(x):
    for i in range(x):
        if row[i] == row[x]:
            return False

        if abs(x - i) == abs(row[x] - row[i]):
            return False

    return True

def sol(x):
    global cnt
    if x == n:
        cnt += 1
        return

    for i in range(n):
        row[x] = i
        if check(x):
            sol(x+1)


sol(0)
print(cnt)