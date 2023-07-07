import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip().strip('['']').split(',')
    que = deque(arr)
    if '' in arr:
        arr = []

    flag = False
    if p.count('D') > len(arr):
        print('error')
        continue

    else:
        for i in p:
            if i == 'D':
                if flag:
                    que.pop()
                else:
                    que.popleft()
            else:
                flag = not(flag)

        if flag:
            que.reverse()

        a = ','.join(que)
        print(f'[{a}]')