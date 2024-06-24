import sys
sys.setrecursionlimit(10**6)

def f(arr, c, depth):
    global gap
    c = c - depth
    if c == 0:
        return
    depth += 1

    mid = len(arr)//2
    if len(arr) / 2 == 0:
        if (arr[-1] - arr[mid]) < (arr[mid] - arr[0]):
            mid -= 1

    left = arr[mid] - arr[0]
    right = arr[-1] - arr[mid]

    gap = min(gap, left,  right)

    f(arr[mid:], c, depth)
    f(arr[0:mid], c, depth)


def solve(arr, c):
    c = c -2
    f(arr, c, 0)
    print(gap)


N, C = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

gap = 1000000000

solve(arr, C)

