n = int(input())
a, b = 100, 100
for i in range(n):
    c, d = map(int, input().split())
    if c > d :
        b = b - c
    elif c < d:
        a = a- d

print(a)
print(b)
