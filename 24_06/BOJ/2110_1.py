import sys
sys.setrecursionlimit(10*6)


def f(arr, c, depth):
    global gap

    if c <= 0:
        return

    c = c - 2 ** depth

    mid = len(arr)//2
    left = arr[mid] - arr[0]
    right = arr[-1] - arr[mid]
    gap = min(gap, left, right)
    if left > right:
        f(arr[0:mid+1], c, depth + 1)
        f(arr[mid:], c, depth + 1)

    else:
        f(arr[mid:], c, depth + 1)
        f(arr[0:mid+1], c, depth + 1)


N, C = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
gap = 10*9
C -= 2

f(arr, C, 0)
print(gap)
