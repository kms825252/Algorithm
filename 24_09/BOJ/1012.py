import sys
from collections import deque

'''
34088KB 60ms

주어진 맵에서 상하좌우로 이어진 땅을 하나의 덩어리로 생각하고
덩어리의 수를 구하면됨
대각선은 이어진거 아님


@수정사항 
1. 완전탐색으로 BFS -> 배추가 있는 좌표를 저장 후 그 좌표들만 BFS
2. 방문을 안한 곳만 BFS
3. BFS에서 큐에 좌표를 넣고 바로 방문처리하여 중복 방문을 막음
'''


def BFS(x, y):
    global cnt
    global arr

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for w in range(4):
            l, r = direction[w]
            new_x = x + l
            new_y = y + r
            if 0 <= new_x < M and 0 <= new_y < N:
                if arr[new_y][new_x] == 1:
                    q.append((new_x, new_y))
                    arr[new_y][new_x] = 2

    cnt += 1


T = int(sys.stdin.readline())
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    cnt = 0
    location = []

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
        location.append((x, y))

    for x, y in location:
        if arr[y][x] == 1:
            BFS(x, y)

    print(cnt)