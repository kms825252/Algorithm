T = int(input())
for _ in range(T):
    a = list(input())
    stk = []
    try:
        for i in range(len(a)):
            if a[i] == '(':
                stk.append(a[i])

            else:
                stk.pop()
        if stk:
            print('NO')
        else:
            print('YES')

    except:
        print('NO')

