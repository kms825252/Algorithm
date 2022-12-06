t = int(input())
a = []
for _ in range(t):
    name, day, month, year = input().split()
    if int(day) < 10:
        day = '0' + day
    if int(month) < 10:
        month = '0' + month
    birth = int(year + month + day)
    a.append((birth,name))

a.sort()
print(a[-1][1])
print(a[0][1])