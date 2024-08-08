from sys import stdin as ss
from collections import deque


'''
시간초과
루프를 돌면서 계속 정렬을 하기 때문에 시간 초과
'''

N = int(ss.readline())
heap = deque()
result = 0
temp = 0

for _ in range(N):
    heap.append(int(ss.readline()))

heap = deque(sorted(heap))

while len(heap) - 1:
    temp1 = heap.popleft()
    temp2 = heap.popleft()
    temp = temp1 + temp2
    heap.append(temp)
    heap = deque(sorted(heap))
    result += temp


print(result)