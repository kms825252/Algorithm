from sys import stdin as ss
import heapq


'''
53408KB 1396ms

heapq를 이용하여 다익스트라
'''

def dijkstra(node):
    q = []
    heapq.heappush(q, (node, 0))
    time_table[node] = 0

    while q:
        new_node, new_sec = heapq.heappop(q)

        if time_table[new_node] < new_sec:
            continue

        for i in relation[new_node]:
            if new_sec + i[1] < time_table[i[0]]:
                time_table[i[0]] = new_sec + i[1]
                heapq.heappush(q, (i[0], time_table[i[0]]))



tc = int(ss.readline())
INF = 1e9

for _ in range(tc):
    n, d, c = map(int, ss.readline().split())
    relation = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    time_table = [INF] * (n+1)
    cnt = 0
    sec = 0

    for _ in range(d):
        a, b, s = map(int, ss.readline().split())
        relation[b].append((a, s))

    dijkstra(c)

    for i in range(1, n+1):
        if time_table[i] != 1e9:
            cnt += 1
            if time_table[i] > sec:
                sec = time_table[i]

    print(cnt, end=' ')
    print(sec)
