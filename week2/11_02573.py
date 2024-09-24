import sys
from collections import deque
n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
graph = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
d = [[0, 1],[1, 0],[0, -1],[-1, 0]]
queue = deque()
result = 0

for y in range(n):
  for x in range(m):
    if graph[y][x] == 0:
      continue
    queue.append((y, x))

def check(y, x):
  return 0 <= y and y < n and 0 <= x and x < m

def bfs(iy, ix):
  q = deque()
  q.append((iy, ix))
  visited = [[False] * m for _ in range(n)]
  visited[iy][ix] = True
  cnt = 1
  while q:
    y, x = q.popleft()
    for dy, dx in d:
      ny, nx = dy + y, dx + x
      if not check(ny, nx):
        continue
      if visited[ny][nx]:
        continue
      if graph[ny][nx] == 0:
        continue
      cnt += 1
      visited[ny][nx] = True
      q.append((ny, nx))
  return cnt

while True:
  result += 1
  l = len(queue)
  _is = False
  is_melted = [[False] * m for _ in range(n)]
  for i in range(l):
    y, x = queue.popleft()
    for dy, dx in d:
      ny, nx = dy + y, dx + x
      if not check(ny, nx):
        continue
      if is_melted[ny][nx]:
        continue
      if graph[ny][nx] > 0:
        continue
      _is = True
      graph[y][x] -= 1
      if graph[y][x] == 0:
        is_melted[y][x] = True
        break
    if graph[y][x] > 0:
      queue.append([y, x])

  if not _is or len(queue) == 0:
    print(0)
    break
  
  if bfs(queue[0][0], queue[0][1]) != len(queue):
    print(result)
    break
