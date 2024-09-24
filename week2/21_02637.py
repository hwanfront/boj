import sys
from collections import deque
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
edges = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
queue = deque()
result = 0
obj = {}

for a, b, c in edges:
  graph[b].append((a, c))
  degree[a] += 1

for i in range(1, n + 1):
  if degree[i] == 0:
    queue.append(i)
    obj[i] = 0

cnt = [obj.copy() for _ in range(n + 1)]

for key in obj.keys():
  cnt[key][key] = 1

while queue:
  node = queue.popleft()
  last = node
  for next, cost in graph[node]:
    for key in obj.keys():
      cnt[next][key] += cnt[node][key] * cost
    degree[next] -= 1
    if degree[next] == 0:
      queue.append(next)

result = []
for key, value in cnt[node].items():
  result.append(f'{key} {value}')

print('\n'.join(result))