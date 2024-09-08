from sys import stdin as ss
from sys import setrecursionlimit

'''
DFS 메모리 초과
'''


setrecursionlimit(10**7)

def DFS(node, visited):
    global cnt

    visited[node] = 1

    for new_node in relation[node]:
        if not visited[new_node]:
            DFS(new_node, visited)
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
    DFS(i, visited)
    if cnt > max_value:
        max_value = cnt
        computer = [i]

    elif cnt == max_value:
        computer.append(i)

for i in computer:
    print(i, end= ' ')

