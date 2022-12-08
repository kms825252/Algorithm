for _ in range(3):
    a, b, c, d = map(int, input().split())
    my_sum = a + b + c + d
    if my_sum == 3:
        print('A')

    elif my_sum == 2:
        print('B')

    elif my_sum == 1:
        print('C')

    elif my_sum == 0:
        print('D')

    else:
        print('E')