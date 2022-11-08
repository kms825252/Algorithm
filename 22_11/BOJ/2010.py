import sys

n = int(sys.stdin.readline())
plug = 0
for _ in range(n):
    a = int(sys.stdin.readline())
    plug += a
plug -= (n-1)
print(plug)