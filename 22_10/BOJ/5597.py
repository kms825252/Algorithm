cnt = [0] * 31
cnt[0] = 1
for i in range(28):
    a = int(input())
    cnt[a] = 1

for j in range(31):
    if cnt[j] == 0:
        print(j)