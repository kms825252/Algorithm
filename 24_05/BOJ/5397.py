import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    keylog = sys.stdin.readline().rstrip()
    pw = deque()
    idx = 0
    for i in keylog:
        if i == '<':
            if idx != 0:
                idx -= 1

        elif i == '>':
            if len(pw) > idx:
                idx += 1

        elif i == '-':
            if idx != 0:
                del(pw[idx -1])
                idx -= 1

        else:
            pw.insert(idx, i)
            idx += 1

    print(''.join(pw))