while True:
    a = int(input())
    if a == -1:
        break

    num = []
    for i in range(1, a//2+1):
        if a % i == 0:
           num.append(i)

    if sum(num) == a:
        print(f'{a} =', end=' ')
        for j in range(len(num)):
            if j!=0:
                print(f'+ {num[j]}', end=' ')
            else:
                print(num[j], end=' ')
        print()
    else:
        print(f'{a} is NOT perfect.')