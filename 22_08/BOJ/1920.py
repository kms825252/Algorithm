import sys

def sol(i, num, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if i == num[mid]:
        return 1
    elif i < num[mid]:
        return sol(i, num, start, mid-1)
    elif i > num[mid]:
        return sol(i, num, mid+1, end)

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
case = list(map(int, sys.stdin.readline().split()))
num.sort()

for i in case:
    start = 0
    end = len(num)-1
    print(sol(i, num, start, end))