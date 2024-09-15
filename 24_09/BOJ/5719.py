from sys import stdin as ss
import heapq

INF = 10**4

def dijkstra(n):
    heap = []
    heapq.heappush(heap, (0, n))
    path_table[n] = 0

    while heap:
        length, node = heapq.heappop(heap)

        if path_table[node] < length:
            continue

        for new_length, new_node in road[node]:
            if length + new_length < path_table[new_node]:
                path_table[new_node] = length + new_length
                heapq.heappush(heap, (path_table[new_node], new_node))

                if new_node == D:
                    result[path_table[new_node]] = 1




while True:
    N, M = map(int, ss.readline().split())
    if N == 0 and M == 0:
        break

    road = [[] for _ in range(N)]
    path_table = [INF] * N
    result = [0] * (10**3 + 1)
    cnt = 0

    S, D = map(int, ss.readline().split())

    for i in range(M):
        U, V, P = map(int, ss.readline().split())
        road[U].append((P, V))

    dijkstra(S)
    print(result)

    for i in range(10**3 + 1):
        if result[i]:
            cnt += 1
            if cnt == 2:
                print(i)
                break
    else:
        print(-1)
