from sys import stdin as ss
'''
31120KB 32ms

1번 컴퓨터 바이러스
바이러스 걸린 컴퓨터의 수 출력

DFS(재귀)를 이용하여 1번과 연결된 모든 컴퓨터를 탐색
탐색을 하며 count를 함

1번 컴퓨터를 제외한 컴퓨터 수를 출력하기 때문에 마지막에 -1를 함
'''


def DFS(node, network, visited):
    global cnt

    visited[node] = 1
    cnt += 1
    for new_node in network[node]:
        if not visited[new_node]:
            DFS(new_node, network, visited)

    return cnt


N = int(ss.readline())
K = int(ss.readline())
network = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(K):
    a, b = map(int, ss.readline().split())
    network[a].append(b)
    network[b].append(a)

print(DFS(1, network, visited) - 1)