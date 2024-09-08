from sys import stdin as ss
from collections import deque

'''
210764KB 11052ms
BFS pypy3로 통과
'''

def BFS(node):
    global cnt

    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        v = q.popleft()
        for new_node in relation[v]:
            if not visited[new_node]:
                q.append(new_node)
                visited[new_node] = 1
                cnt += 1


N, M = map(int, ss.readline().split())
relation = [[] for _ in range(N+1)]
computer = []
max_value = 0

for _ in range(M):
    a, b = map(int, ss.readline().split())
    relation[b].append(a)

for i in range(1, N+1):
    visited = [0] * (N + 1)
    cnt = 0
    BFS(i)
    if cnt > max_value:
        max_value = cnt
        computer = [i]

    elif cnt == max_value:
        computer.append(i)

for i in computer:
    print(i, end=' ')

