import sys
from collections import deque
n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().strip() for _ in range(n)]
d = ((0, 1),(1, 0),(0, -1),(-1, 0))

def check(y, x):
  return 0 <= y and y < n and 0 <= x and x < n

def bfs():
  queue = deque()
  queue.append((0, 0, 0))
  visited = [[-1] * n for _ in range(n)]
  visited[0][0] = 0

  while queue:
    y, x, cost = queue.popleft()
    if y == n - 1 and x == n - 1:
      return cost
    for dy, dx in d:
      ny, nx = dy + y, dx + x
      if not check(ny, nx):
        continue
      if data[ny][nx] == '0':
        if visited[ny][nx] >= cost + 1:
          continue
        visited[ny][nx] = cost + 1
        queue.append((ny, nx, cost + 1))
        continue
      if visited[ny][nx] >= cost:
        continue
      visited[ny][nx] = cost
      queue.appendleft((ny, nx, cost))

print(bfs())