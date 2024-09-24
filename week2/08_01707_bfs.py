import sys
from collections import deque
k = int(sys.stdin.readline().strip())
result = []

def bfs(graph, visited, start):
  queue = deque()
  queue.append((start, -1))
  visited[i] = -1

  while queue:
    node, color = queue.popleft()
    for next in graph[node]:
      if visited[next] == color:
        return False
      if visited[next] == 0:
        visited[next] = -color
        queue.append((next, -color))

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
    if not bfs(graph, visited, i):
      _is = False
      break
  result.append('YES' if _is else 'NO')

print('\n'.join(result))