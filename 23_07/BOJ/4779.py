def sol(x):
    if len(x) < 2:
        return x
    a = len(x) // 3
    first = sol(x[:a])
    second = sol(x[a:(2 * a)])
    third = sol(x[(2 * a):])

    second = second.replace('-', ' ')

    sum_word = first + second + third
    return sum_word


while True:
    try:
        n = int(input())
        x = '-' * (3**n)
        print(sol(x))
    except:
        break