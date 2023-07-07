from collections import deque
import sys

input = sys.stdin.readline
que = deque()

N = int(input())
for _ in range(N):
    com = list(input().split())
    if com[0] == 'push_front':
        que.appendleft(int(com[1]))

    elif com[0] == 'push_back':
        que.append(int(com[1]))

    elif com[0] == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif com[0] == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)

    elif com[0] == 'size':
        print(len(que))

    elif com[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)

    elif com[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif com[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
