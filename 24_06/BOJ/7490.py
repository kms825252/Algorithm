from sys import stdin as ss


def cal(arr):
    ans = arr[0]
    for i in range(1,len(arr),2):
        if arr[i] == '+':
            ans = ans + arr[i+1]
        elif arr[i] == '-':
            ans = ans - arr[i+1]
    return ans


def solve(idx, arr, sign):
    global result
    global n

    arr.insert(idx, sign)
    if idx == ((n * 2) - 3):
        if cal(arr) == 0:
            result.append(arr)
        return
    solve(idx+2, arr, '+')
    solve(idx+2, arr, '-')

    return result


tc = int(ss.readline())

for _ in range(tc):
    result = []
    n = int(ss.readline())
    n_list = list(range(1, n+1))
    solve(1, n_list,'+')
    solve(1, n_list,'-')
    print(result)


