import sys
from collections import deque
n, k = tuple(map(int, sys.stdin.readline().strip().split(' ')))
data = [int(sys.stdin.readline().strip()) for _ in range(n)]
visited = [False] * (k + 1)

def bfs():
  queue = deque()
  queue.append((k, 0))
  visited[k] = True

  while queue:
    total, cnt = queue.popleft()
    if total == 0:
      return cnt
    for v in data:
      if total - v < 0:
        continue
      if visited[total - v]:
        continue
      visited[total - v] = True
      queue.append((total - v, cnt + 1))
  return -1

print(bfs())
