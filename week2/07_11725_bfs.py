import sys
from collections import deque
n = int(sys.stdin.readline().strip())
edges = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n - 1)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) 
result = [0] * (n + 1)

for a, b in edges:
  graph[a].append(b)
  graph[b].append(a)

def bfs():
  queue = deque()
  queue.append(1)
  visited[1] = True

  while queue:
    node = queue.popleft()
    for next in graph[node]:
      if visited[next]:
        continue
      visited[next] = True
      queue.append(next)
      result[next] = node

bfs()

print('\n'.join(map(str, result[2:])))