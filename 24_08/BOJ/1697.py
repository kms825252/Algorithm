from sys import stdin as ss
from collections import deque

'''
39208KB 148ms

조건 
1. 둘다 위치가 같을때
2. 수빈이 이동 위치 제한

visited를 만들어서 이전에 이동했던 값에 중복을 피함


'''

def BFS(n, k, visited):
    x = [2, 1, -1]
    q = deque()
    q.append(n)
    flag = 0
    visited[n] = 1

    if n == k:
        print(0)
        return

    while q:
        point = q.popleft()

        for i in range(3):
            if not i:
                new_point = point * x[i]
                if 0 < new_point < 200000 and not visited[new_point]:
                    visited[new_point] = visited[point] + 1
                    q.append(new_point)
                    if new_point == k:
                        flag = 1
                        break

            else:
                new_point = point + x[i]
                if 0 <= new_point < 200000 and not visited[new_point]:
                    visited[new_point] = visited[point] + 1
                    q.append(new_point)
                    if new_point == k:
                        flag = 1
                        break

        if flag:
            break
    print(visited[k] - 1)

N, K = map(int, ss.readline().split())
visited = [0] * 200001

BFS(N, K, visited)
