t = int(input())
for _ in range(t):
    n = int(input())
    case = {}
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        case[a] = b
    print(max(case, key=case.get))
