from collections import deque

MAX = 100001
n, k = map(int, input().split())
arr = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return arr[now_pos]
        for next_pos in (now_pos -1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < MAX and not arr[next_pos]:
                arr[next_pos] = arr[now_pos] + 1
                q.append(next_pos)

print(bfs())