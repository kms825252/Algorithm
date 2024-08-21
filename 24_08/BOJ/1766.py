from sys import stdin as ss
import heapq

'''
40128KB 6248ms
'''

N, M = map(int, ss.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, ss.readline().split())
    heapq.heappush(graph[a], b)
    indegree[b] += 1

def solve():
    result = []
    heap = []
    for i in range(1, N+1):
        if i in result:
            continue
        if indegree[i] == 0 and i not in heap:
            heapq.heappush(heap, i)

        while heap:
            now = heapq.heappop(heap)
            if now > i+1:
                heapq.heappush(heap, now)
                break
            result.append(now)
            for j in graph[now]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    heapq.heappush(heap, j)

    for i in result:
        print(i, end=' ')

solve()