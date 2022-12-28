n = int(input())
room = []
for _ in range(n):
    room.append(list(input()))

garo = [0] * n
for i in range(n):
    for j in range(n-1):
        if room[i][j] == '.' and room[i][j+1] == '.':
            garo[i] = 1
            break

sero = [0] * n
for k in range(n-1):
    for l in range(n):
        if room[k][l] == '.' and room[k+1][l] == '.':
            sero[l] = 1

print(sum(garo), sum(sero))
