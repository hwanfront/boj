import sys
from collections import deque
n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
edges = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for a, b in edges:
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  queue = deque()
  queue.append(start)
  visited[start] = True

  while len(queue) != 0:
    node = queue.popleft()
    for next in graph[node]:
      if visited[next]:
        continue
      visited[next] = True
      queue.append(next)

for i in range(1, n + 1):
  if visited[i]:
    continue
  result += 1
  bfs(i)

print(result)
