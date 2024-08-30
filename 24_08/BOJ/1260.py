from sys import stdin as ss
from collections import deque

'''
34052KB 64ms

DFS는 재귀를 이용
BFS는 deque를 이용하여 구현

단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다.

위의 조건을 보지 못하여 예제2번이 막힘
-> 작은 것부터 방문하기 위해 간선 그래프를 만들고 그것을 순회하며 sort를 했다.
'''

def DFS(graph, v, visited):
    print(v, end=' ')
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

N, M, V = map(int, ss.readline().split())
graph = [[] for _ in range(N+1)]


def BFS(graph, v, visted):
    q = deque()
    q.append(v)

    while q:
        node = q.popleft()
        if not visted[node]:
            visited[node] = 1
            print(node, end=' ')
            for i in graph[node]:
                    q.append(i)

    return 0


for _ in range(M):
    a, b = map(int, ss.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [0]*(N+1)
DFS(graph, V, visited)
print()
visited = [0]*(N+1)
BFS(graph, V, visited)
