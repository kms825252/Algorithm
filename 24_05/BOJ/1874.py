from sys import stdin
from collections import deque

n = int(stdin.readline())
num = deque()
stack = deque()
result = []

for i in range(n):
    num.append(int(stdin.readline()))

for i in range(1, n+1):
    stack.append(i)
    result.append('+')

    while stack:
        if num[0] == stack[-1]:
            num.popleft()
            stack.pop()
            result.append('-')

        else:
            break

if stack:
    print('NO')

else:
    for i in result:
        print(i)