from collections import deque

def dfs(v):
    stack = []
    stack.append(v)
    while stack:
        s = stack.pop()
        if not visited[s]:
            print(s, end=' ')
            visited[s] = 1
            for e in adj[s]:
                if not visited[e]:
                    stack.append(e)

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = 1
            print(v, end = ' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)


n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [0]*(n +1)
dfs(v)
print()
visited = [0] *(n + 1)
bfs(v)
'''
1 2 4 3 
'''