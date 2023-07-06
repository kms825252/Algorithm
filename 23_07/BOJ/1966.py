import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    que = deque()
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        que.append([a[i], i])

    order = 0
    while True:
        if max(que)[0] != que[0][0]:
            paper = que.popleft()
            que.append(paper)
        else:
            order += 1
            if que[0][1] == M:
                break
            else:
                que.popleft()
    print(order)
