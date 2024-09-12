import sys
from queue import Queue

def check(y, x):
  return 0 <= y and y < n and 0 <= x and x < n

def go(iy, ix, h):
  global visited
  q = Queue()
  q.put([iy, ix])
  visited[iy][ix] = 1
  while not q.empty():
    [y, x] = q.get()
    for [dy, dx] in d:
      [ny, nx] = [dy + y, dx + x]
      if not check(ny, nx): continue
      if visited[ny][nx] == 1: continue
      if area[ny][nx] <= h: continue
      visited[ny][nx] = 1
      q.put([ny, nx])


n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
d = [[0, 1],[1, 0],[0, -1],[-1, 0]]
visited = [[0 for _ in range(0, n)] for __ in range(0, n)]
hh = []
result = 1

for y in range(0, n):
  for x in range(0, n):
    hh.append(area[y][x])

hh = list(set(hh))

for h in hh:
  cnt = 0
  for y in range(0, n):
    for x in range(0, n):
      visited[y][x] = 0
  for y in range(0, n):
    for x in range(0, n):
      if area[y][x] <= h: continue
      if visited[y][x] == 1: continue
      go(y, x, h)
      cnt += 1
  result = max(result, cnt)

print(result)