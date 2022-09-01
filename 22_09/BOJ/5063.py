T = int(input())
for tc in range(1, T+1):
    r, e, c = map(int, input().split())

    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    elif r < e - c :
        print('advertise')