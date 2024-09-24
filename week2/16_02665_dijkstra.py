import sys
import heapq
n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().strip() for _ in range(n)]
d = ((0, 1),(1, 0),(0, -1),(-1, 0))
INF = 10 ** 9

def check(y, x):
  return 0 <= y and y < n and 0 <= x and x < n

def dijkstra():
  pq = [(0, 0, 0)]
  dist = [[INF] * n for _ in range(n)]
  dist[0][0] = 0

  while pq:
    y, x, cost = heapq.heappop(pq)

    for dy, dx in d:
      ny, nx = dy + y, dx + x
      if not check(ny,nx):
        continue
      c_cost = 1 if data[ny][nx] == '0' else 0
      if dist[ny][nx] > c_cost + cost:
        dist[ny][nx] = c_cost + cost
        heapq.heappush(pq, (ny, nx, dist[ny][nx]))
  return dist[n - 1][n - 1]

print(dijkstra())