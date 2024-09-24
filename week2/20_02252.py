import sys
from collections import deque
n, m = tuple(map(int, sys.stdin.readline().strip().split(' ')))
data = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
queue = deque()
result = []

for a, b in data:
  degree[b] += 1
  graph[a].append(b)

for i in range(1, n + 1):
  if degree[i] == 0:
    queue.append(i)

while queue:
  node = queue.popleft()
  result.append(node)
  for next in graph[node]:
    degree[next] -= 1
    if degree[next] == 0:
      queue.append(next)

print(' '.join(map(str, result)))