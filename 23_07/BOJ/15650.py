n, m = map(int, input().split())
ans = []


def sol(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, n+ 1):
        ans.append(i)
        sol(i+1)
        ans.pop()

sol(1)