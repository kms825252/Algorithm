from sys import stdin as ss
import itertools


N, K = map(int, ss.readline().split())
goods = []
max_value = 0
bag = [[] for _ in range(N+1)]

for i in range(1, N+1):
    a, b = map(int, ss.readline().split())
    goods.append((a, b))

for good in goods:
    if good[0] <= K:
        bag[1].append(good)
        if max_value < good[1]:
            max_value = good[1]

for i in range(2,N+1):
    temp = list(itertools.combinations(bag[i-1], i))
    for goods in temp:
        weight = 0
        value = 0
        for good in goods:
            weight += good[0]
            value += good[1]

        if weight <= K:
            for k in goods:
                bag[i].append(k)
            if max_value < value:
                max_value = value
    set(bag[i])

print(max_value)