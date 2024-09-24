import sys
from collections import deque
r, c = tuple(map(int, sys.stdin.readline().strip().split(' ')))
data = [list(sys.stdin.readline().strip()) for _ in range(r)]
d = ((0, 1),(1, 0),(0, -1),(-1, 0))
water = []

for y in range(r):
  for x in range(c):
    if data[y][x] == '.':
      continue
    if data[y][x] == 'D':
      continue
    if data[y][x] == 'X':
      continue
    if data[y][x] == 'S':
      s = [y, x]
      data[y][x] = '.'
      continue
    water.append((y, x))

def check(y, x):
  return 0 <= y and y < r and 0 <= x and x < c
    
def bfs(s, water):
  queue1 = deque(water)
  queue2 = deque([s])
  visited = [[False] * c for _ in range(r)]
  visited[s[0]][s[1]] = True
  cnt = 0

  while queue2:
    l1 = len(queue1)
    l2 = len(queue2)

    for _ in range(l1):
      y, x = queue1.popleft()
      for dy, dx in d:
        ny, nx = dy + y, dx + x
        if not check(ny, nx):
          continue
        if data[ny][nx] == '*' or data[ny][nx] == 'D' or data[ny][nx] == 'X':
          continue
        data[ny][nx] = '*'
        queue1.append((ny, nx))

    for _ in range(l2):
      y, x = queue2.popleft()
      for dy, dx in d:
        ny, nx = dy + y, dx + x
        if not check(ny, nx):
          continue
        if visited[ny][nx]:
          continue
        if data[ny][nx] == '*' or data[ny][nx] == 'X':
          continue
        if data[ny][nx] == 'D':
          return cnt + 1
        visited[ny][nx] = True
        queue2.append((ny, nx))
    
    cnt += 1
  return 'KAKTUS'

print(bfs(s, water))

  