t= int(input())
case = [[0] * 101 for _ in range(101)]

for _ in range(t):
    a, b = map(int, input().split())
    for i in range(b, b+10):
        for j in range(a, a+10):
            case[i][j] = 1

cnt = 0
for k in range(101):
    cnt += case[k].count(1)

print(cnt)