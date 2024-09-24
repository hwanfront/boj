import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline().strip())
result = []

def dfs(graph, visited, node, color = 1):
  for next in graph[node]:
    if visited[next] == color:
      continue
    if visited[next] == 0:
      visited[next] = color
      if not dfs(graph, visited, next, -1 if color == 1 else 1):
        return False
      continue
    return False
  return True

for __ in range(k):
  v, e = list(map(int, sys.stdin.readline().strip().split(' ')))
  visited = [0] * (v + 1)
  graph = [[] for _ in range(v + 1)]
  for _ in range(e):
    a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
    graph[a].append(b)
    graph[b].append(a)
  _is = True
  for i in range(1, v + 1):
    if visited[i] != 0:
      continue
    visited[i] = -1
    if not dfs(graph, visited, i):
      _is = False
      break
  result.append('YES' if _is else 'NO')

print('\n'.join(result))