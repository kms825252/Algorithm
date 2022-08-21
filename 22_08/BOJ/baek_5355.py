T = int(input())
for tc in range(1, T+1):
    a = list(input().split())
    a[0] = float(a[0])

    for i in a:
        if i == '@':
            a[0] = a[0] * 3
        
        if i == '%':
            a[0] = a[0] + 5

        if i == '#':
            a[0] = a[0] - 7
            
    print(f'{a[0]:.2f}')
