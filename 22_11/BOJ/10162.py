a = 300
b = 60
c = 10
a_btn=0
b_btn=0
c_btn=0

n = int(input())

while True:
    if n == 0:
        print(a_btn, b_btn, c_btn)
        break

    elif n >= a:
        n = n - a
        a_btn += 1

    elif n >= b:
        n = n - b
        b_btn += 1

    elif n >= c:
        n = n - c
        c_btn += 1

    else:
        print(-1)
        break

