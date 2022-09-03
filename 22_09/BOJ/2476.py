T = int(input())
money = []
for tc in range(1, T+1):
    a, b, c  = map(int, input().split())
    if a == b and b == c:
        money.append(10000 + a*1000)
    elif a == b:
        money.append(1000 + a*100)
    elif b == c:
        money.append(1000 + b*100)
    elif c == a:
        money.append(1000 + c*100)
    else:
        money.append(max(a,b,c) * 100)

print(max(money))