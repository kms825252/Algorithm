T = int(input())
for _ in range(T):
    VPS = list(input())
    cnt = 0
    for i in range(len(VPS)):
        if VPS[i] == '(':
            cnt += 1
        else:
            if cnt <= 0:
                print('NO')
                break
            else:
                cnt -= 1
    else:
        if cnt:
            print('NO')
        else:
            print('YES')