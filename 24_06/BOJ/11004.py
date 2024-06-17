from sys import stdin as ss

'''623188KB 3884ms'''
N, K = map(int, ss.readline().split())
num_list = list(map(int, ss.readline().split()))

num_list.sort()

print(num_list[K-1])