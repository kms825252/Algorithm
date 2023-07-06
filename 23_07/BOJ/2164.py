import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for i in range(1,N+1):
    que.append(i)

while len(que) > 1:
    que.popleft()
    num = que.popleft()
    que.append(num)

print(que[0])