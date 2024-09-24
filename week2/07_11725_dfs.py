import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().strip())
edges = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n - 1)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) 
result = [0] * (n + 1)

for a, b in edges:
  graph[a].append(b)
  graph[b].append(a)

def dfs(node):
  for next in graph[node]:
    if visited[next]:
      continue
    visited[next] = True
    result[next] = node
    dfs(next)

visited[1] = True
dfs(1)

print('\n'.join(map(str, result[2:])))