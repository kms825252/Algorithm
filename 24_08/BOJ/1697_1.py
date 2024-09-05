from sys import stdin as ss
from collections import deque

'''
39208KB 148ms

@조건 
1. 둘다 위치가 같을때
2. 수빈이 이동 위치 제한

visited를 만들어서 이전에 이동했던 값에 중복을 피함

@수정사항
1. 큐에서 새로운 위치값을 가져올때 동생 위치를 비교해서 flag를 없앰
2. new_point를 만들때 2배, +1, -1이 계산된 값을 가져와서 조건을 수행함으로서 중복코드를 줄임
'''

def BFS(n, k, visited):
    q = deque()
    q.append(n)
    visited[n] = 1

    while q:
        point = q.popleft()
        if point == k:
            print(visited[point] - 1)

        for new_point in (point*2, point+1, point-1):
            if 0 <= new_point < 200000 and not visited[new_point]:
                visited[new_point] = visited[point] + 1
                q.append(new_point)

N, K = map(int, ss.readline().split())
visited = [0] * 200001

BFS(N, K, visited)
