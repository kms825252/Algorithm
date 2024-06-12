from sys import stdin as ss
import copy

'''31716KB 136ms'''
def solve(arr, num):
    global result
    global N

    arr.append(str(num))

    if len(arr) == (2 * N - 1):
        if eval(''.join(arr).replace(' ', '')) == 0:
            a = copy.deepcopy(arr)
            result.append(a)
        return

    arr.append(' ')
    solve(arr, num+1)
    arr.pop()
    arr.pop()

    arr.append('+')
    solve(arr, num+1)
    arr.pop()
    arr.pop()

    arr.append('-')
    solve(arr, num+1)
    arr.pop()
    arr.pop()

    num += 1

tc = int(ss.readline())
for i in range(tc):
    num = 1
    arr = []
    result = []
    N = int(ss.readline())
    solve(arr, 1)
    for i in result:
        print(''.join(i))
    print()