import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
edges = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for a, b in edges:
  graph[a].append(b)
  graph[b].append(a)

def dfs(node):
  global result
  for next in graph[node]:
    if visited[next]:
      continue
    visited[next] = True
    result += 1
    dfs(next)

visited[1] = True
dfs(1)

print(result)