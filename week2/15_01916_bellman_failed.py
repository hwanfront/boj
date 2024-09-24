import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
bus_infos = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
start, end = tuple(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10 ** 9
graph = [[] for _ in range(n + 1)]

def bellman():
  dist = [INF] * (n + 1)
  dist[start] = 0

  for _ in range(n - 1):
    print(dist)
    for a, b, cost in bus_infos:
      if dist[b] > dist[a] + cost:
        dist[b] = dist[a] + cost

  return dist[end]

print(bellman())
