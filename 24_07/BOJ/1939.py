from sys import stdin as ss


'''
한 번의 이동에서 옮길 수 있는 물품들의 중량 최댓값


'''
N, M = map(int, ss.readline().split())
bridge = [[] for _ in range(N+1)]
weight = [0] * (M + 1)

for _ in range(M):
    A, B, C = map(int, ss.readline().split())
    bridge[A].append((B, C))
    bridge[B].append((A, C))

def get_biggest_node():
    max_value = 0
    idx = 0
    for i in range(1, )