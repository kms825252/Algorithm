# 시간 초과

# import sys
#
# T = int(sys.stdin.readline())
# stack = [0] * 100
# front = -1
# rear = -1
# for tc in range(1, T+1):
#     word =list(sys.stdin.readline().split())
#     if word[0] == 'push':
#         rear += 1
#         stack[rear] = word[1]
#
#     elif word[0] == 'pop':
#         if front != rear:
#             front += 1
#             print(stack[front])
#         else:
#             print(-1)
#
#     elif word[0] == 'front':
#         if front != rear :
#             front += 1
#             print(stack[front])
#             front -= 1
#         else:
#             print(-1)
#
#     elif word[0] =='back':
#         if front != rear :
#             print(stack[rear])
#
#         else:
#             print(-1)
#
#     elif word[0] == 'size':
#         print(rear - front)
#
#     elif word[0] == 'empty':
#         if front == rear:
#             print(1)
#         else:
#             print(0)

import sys
from collections import deque

T = int(sys.stdin.readline())
q = deque()
for tc in range(T):
    case = sys.stdin.readline().split()

    if case[0] =='push':
        q.append(case[1])
    elif case[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif case[0] == 'size':
        print(len(q))

    elif case[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif case[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif case[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)



