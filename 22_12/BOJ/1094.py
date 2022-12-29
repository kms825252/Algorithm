n = int(input())
stick = 64
ans = []
while stick > 0:
    if (n - stick) >= 0:
        n = n - stick
        ans.append(stick)
    stick = stick//2


print(len(ans))