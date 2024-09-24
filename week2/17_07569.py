import sys
from collections import deque
m, n, h = tuple(map(int, sys.stdin.readline().strip().split(' ')))
data = [sys.stdin.readline().strip().split(' ') for _ in range(n * h)]
d1 = ((0, 1),(1, 0),(0, -1),(-1, 0))
d2 = (n, -n)
queue = deque()
visited = [[False] * m for _ in range(n * h)]
tmt_cnt = 0
emp_cnt = 0

for y in range(n * h):
  for x in range(m):
    if data[y][x] == '1':
      queue.append((y, x))
      visited[y][x] = True
      tmt_cnt += 1
      continue
    if data[y][x] == '-1':
      emp_cnt += 1

if tmt_cnt + emp_cnt == (n * h) * m:
  print(0)
  exit()

def check1(prev_y, y, x):
  return 0 <= x and x < m and (prev_y // n) * n <= y and y < ((prev_y // n) * n + n)
def check2(y):
  return 0 <= y and y < (n * h)

def bfs(queue):
  global tmt_cnt
  res = 0
  while queue:
    l = len(queue)
    res += 1
    for _ in range(l):
      y, x = queue.popleft()
      for dy, dx in d1:
        ny, nx = dy + y, dx + x
        if not check1(y, ny, nx):
          continue
        if visited[ny][nx]:
          continue
        if data[ny][nx] == '-1':
          continue
        visited[ny][nx] = True
        data[ny][nx] = '1'
        queue.append((ny, nx))
        tmt_cnt += 1

      for dy in d2:
        ny = dy + y
        if not check2(ny):
          continue
        if visited[ny][x]:
          continue
        if data[ny][x] == '-1':
          continue
        visited[ny][x] = True
        data[ny][x] = '1'
        queue.append((ny, x))
        tmt_cnt += 1

  return res - 1

result = bfs(queue)
print(result if tmt_cnt + emp_cnt == (n * h) * m else -1)

