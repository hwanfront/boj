# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

import sys
from queue import Queue
n, m, v = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result1 = []
result2 = []

for i in range(m):
  [a, b] = list(map(int, sys.stdin.readline().strip().split()))
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n + 1):
  graph[i].sort()

def dfs(now):
  result1.append(now)
  for next in graph[now]:
    if visited[next]:
      continue
    visited[next] = True
    dfs(next)

def bfs(start):
  queue = Queue()
  queue.put(start)
  visited[start] = True

  while not queue.empty():
    now = queue.get()
    result2.append(now)
    for next in graph[now]:
      if visited[next]:
        continue
      visited[next] = True
      queue.put(next)

visited[v] = True
dfs(v)

visited = [False] * (n + 1)
bfs(v)

print(' '.join(map(str, result1)))
print(' '.join(map(str, result2)))