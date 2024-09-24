import sys
from collections import deque
n, m, k, x = tuple(map(int, sys.stdin.readline().strip().split(' ')))
edges = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
result = []

for a, b in edges:
  graph[a].append(b)

def bfs():
  queue = deque()
  visited = [False] * (n + 1)
  queue.append((x, 0))
  visited[x] = True

  while queue:
    node, cost = queue.popleft()
    if cost > k:
      return
    if cost == k:
      result.append(node)
    for next in graph[node]:
      if visited[next]:
        continue
      visited[next] = True
      queue.append((next, cost + 1))

bfs()

if len(result) == 0:
  print(-1)
else:
  result.sort()
  print('\n'.join(map(str, result)))


  