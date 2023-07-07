import sys
from collections import deque
input = sys.stdin.readline
que = deque()

N, M = map(int, input().split())
num = list(map(int, input().split()))

for i in range(1, N+1):
    que.append(i)

cnt = 0
order = 0
while order < M:
    if que[0] == num[order]:
        que.popleft()
        order += 1
    else:
        if len(que)/2 >= que.index(num[order]):
            que.rotate(-1)
            cnt +=1
        else:
            que.rotate(1)
            cnt += 1

print(cnt)