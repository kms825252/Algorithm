from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    result = 0
    n, m = map(int, input().split())
    important = deque(map(int, input().split()))
    for i in range(n):
        important[i] = (important[i], i)

    while important:
        my_max = max(important)[0]
        a = important.popleft()
        if a[0] == my_max:
            result += 1
            if a[1] == m:
                break
        else:
            important.append(a)
    print(result)


