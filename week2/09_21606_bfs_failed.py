import sys
from collections import deque
n = int(sys.stdin.readline().strip())
a = '0' + sys.stdin.readline().strip()
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1)
result = 0

for _ in range(n - 1):
  [f, t] = list(map(int, sys.stdin.readline().strip().split(' ')))
  graph[f].append(t)
  graph[t].append(f)

def bfs(start):
  global cnt
  queue = deque()
  queue.append(start)
  visited[start] = True

  while queue:
    node = queue.popleft()
    for next in graph[node]:
      if a[next] == '1':
        cnt += 1
        continue
      visited[next] = True
      queue.append(next)

for i in range(1, n + 1):
  if visited[i]:
    continue
  if a[i] == '0':
    cnt = 0
    bfs(i)
    result += cnt * (cnt - 1)
  else:
    for next in graph[i]:
      if a[next] == '0':
        continue
      result += 1

print(result)