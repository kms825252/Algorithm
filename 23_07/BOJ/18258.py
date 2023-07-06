from collections import deque
import sys

que = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    com = list(sys.stdin.readline().split())
    if com[0] == 'push':
        que.append(int(com[1]))

    elif com[0] == 'pop':
        if que:
            print(que.popleft())
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