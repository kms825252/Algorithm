n = input()
if int(n) >= 10 :
    n = n[-1]
n = int(n)
car = list(map(int, input().split()))
cnt = 0
for i in car:
    if n == i:
        cnt += 1

print(cnt)