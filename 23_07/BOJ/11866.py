import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
que = deque()

for i in range(1, N+1):
    que.append(i)

arr = []
order = 1
while que :
    if order == K:
        num = que.popleft()
        arr.append(str(num))
        order = 0
    else:
        num = que.popleft()
        que.append(num)
    order += 1

# 출력부분
# print('<', end='')
# for i in arr:
#     if i == arr[-1]:
#         print(i, end='')
#     else:
#         print(i, end=', ')
# print('>')
a = ', '.join(arr)
print(f'<{a}>')