ans = 0
for i in range(8):
    chess = list(input())
    for j in range(8):
        if i%2 == 0 and j%2 == 0:
            if chess[j] == 'F':
                ans += 1
        if i%2 == 1 and j%2 == 1:
            if chess[j] == 'F':
                ans += 1

print(ans)