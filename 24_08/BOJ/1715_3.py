from sys import stdin as ss

'''
시간초과
루프를 돌면서 계속 정렬을 하기 때문에 시간초과
'''

N = int(ss.readline())
heap = []
result = 0
temp = 0
idx = 0

for _ in range(N):
    heap.append(int(ss.readline()))

heap.sort()

for _ in range(N-1):
    temp1 = heap[idx]
    idx += 1
    temp2 = heap[idx]
    idx += 1
    temp = temp1 + temp2
    heap.append(temp)
    heap.sort()
    result += temp


print(result)
