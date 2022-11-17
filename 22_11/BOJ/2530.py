h, m, s = map(int, input().split())
a = int(input())

tmp = a + s
s = tmp%60
tmp = m + tmp//60
m = tmp%60
tmp = h + tmp//60


if tmp >= 24:
    h = tmp-24*(tmp//24)
else:
    h = tmp

print(h, m, s)
