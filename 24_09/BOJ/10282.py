from sys import stdin as ss

tc = int(ss.readline())

for _ in range(tc):
    n, d, c = map(int, ss.readline().split())
    relation = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, ss.readline().split())
        relation[b].append((a, s))

    print(relation)