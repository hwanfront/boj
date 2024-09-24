import sys
n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]
result = 0

for _ in range(m):
  a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
  graph1[a].append(b)
  graph2[b].append(a)

def dfs(now, graph):
  global cnt
  if cnt >= ((n + 1) // 2):
    return True
  for next in graph[now]:
    if visited[next]:
      continue
    visited[next] = True
    cnt += 1
    if dfs(next, graph):
      return True
  
  return False

for i in range(1, n + 1):
  visited = [False] * (n + 1)
  cnt = 0
  if dfs(i, graph1):
    result += 1
    continue
  visited = [False] * (n + 1)
  cnt = 0
  if dfs(i, graph2):
    result += 1

print(result)