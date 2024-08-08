from sys import stdin as ss
import heapq

'''
33972KB 180ms

N == 1일때 조건 필요x
33972KB 172ms
'''

N = int(ss.readline())
heap = []
result = 0
temp = 0

for _ in range(N):
    card = int(ss.readline())
    heapq.heappush(heap, card)

while len(heap) - 1:
    temp1 = heapq.heappop(heap)
    temp2 = heapq.heappop(heap)
    temp = temp1 + temp2
    heapq.heappush(heap, temp)
    result += temp


print(result)