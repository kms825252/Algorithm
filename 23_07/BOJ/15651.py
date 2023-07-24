n, m = map(int, input().split())
ans = []

def sol():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        ans.append(i)
        sol()
        ans.pop()

sol()