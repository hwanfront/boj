import sys
from collections import deque
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
roads = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
s, e = tuple(map(int, sys.stdin.readline().strip().split(' ')))
degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
r_graph = [[] for _ in range(n + 1)]
queue = deque()
dist = [0] * (n + 1)
result = 0

for a, b, cost in roads:
  degree[b] += 1
  graph[a].append((b, cost))
  r_graph[b].append((a, cost))

for i in range(1, n + 1):
  queue.append(i)

while queue:
  node = queue.popleft()

  for next_node, next_cost in graph[node]:
    dist[next_node] = max(dist[next_node], dist[node] + next_cost)
    degree[next_node] -= 1
    if degree[next_node] == 0:
      queue.append(next_node)

queue = deque()
queue.append(e)
visited = [False] * (n + 1)
visited[e] = True

while queue:
  node = queue.popleft()

  for next_node, next_cost in r_graph[node]:
    if dist[node] == next_cost + dist[next_node]:
      result += 1
      if visited[next_node]:
        continue
      visited[next_node] = True
      queue.append(next_node)
      
print(f'{dist[e]}\n{result}')