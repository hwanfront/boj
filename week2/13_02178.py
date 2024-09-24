import sys
from collections import deque
n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
data = [sys.stdin.readline().strip() for _ in range(n)]
direction = [(0, 1),(1, 0),(0, -1),(-1, 0)]

def check(y, x):
  return 0 <= y and y < n and 0 <= x and x < m

def bfs():
  queue = deque()
  visited = [[False] * m for _ in range(n)]
  queue.append((0, 0, 1))
  visited[0][0] = True

  while queue:
    y, x, cost = queue.popleft()
    if y == n - 1 and x == m - 1:
      return cost
    for dy, dx in direction:
      ny, nx = dy + y, dx + x
      if not check(ny, nx):
        continue
      if visited[ny][nx]:
        continue
      if data[ny][nx] == '0':
        continue
      visited[ny][nx] = True
      queue.append((ny, nx, cost + 1))

print(bfs())