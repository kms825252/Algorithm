from sys import stdin as ss
from heapq import heappush, heappop

N = int(ss.readline())
heap = []

for _ in range(N):
    num = int(ss.readline())

    if num != 0:
        heappush(heap, num)

    else:
        if heap:
            print(heappop(heap))

        else:
            print(0)