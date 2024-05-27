import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    important = list(map(int, sys.stdin.readline().split()))
    doc = deque()
    idx = 0
    cnt = 0

    for i in range(n):
        doc.append([i, important[i]])

    important.sort(reverse=True)

    while True:

        tmp = doc.popleft()
        if tmp[1] == important[idx]:
            idx += 1
            cnt += 1
            if tmp[0] == m:
                break
        else:
            doc.append(tmp)

    print(cnt)