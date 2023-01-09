import sys
sys.setrecursionlimit(10 ** 9)
def dfs(x, y):
    for a,b in node[x]:
        if visited[a] == -1:
            visited[a] = y + b
            dfs(a, y+b)

n = int(sys.stdin.readline())
node = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
    node[b].append([a, c])


visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

start =visited.index(max(visited))

visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))