from sys import stdin as ss
from collections import deque

'''
모든 박스를 배로 옮기는데 드는 최소 시간 구하기

조건
1. 크레인은 1분에 1개의 박스만 옮길 수 있다
2. N개의 크레인은 각각 무게 제한이 있다
'''

N = int(ss.readline())
crane_weight = list(map(int, ss.readline().split()))
M = int(ss.readline())
box_weight = list(map(int, ss.readline().split()))

crane_weight.sort(reverse=True)
box_weight.sort(reverse=True)

box_weight = deque(box_weight)

min_time = 0
idx = 0
check = [True for _ in range(M)]

if crane_weight[0] < box_weight[0]:
    print(-1)

else:
    while box_weight:
        for i in range(N):
            for j in range(len(box_weight)):
                box = box_weight.popleft()
                if crane_weight[i] >= box:
                    break
                else:
                    box_weight.append(box)

        min_time += 1

print(min_time)