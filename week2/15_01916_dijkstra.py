import sys
import heapq
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
bus_infos = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
start, end = tuple(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10 ** 9
graph = [[] for _ in range(n + 1)]

for a, b, cost in bus_infos:
  graph[a].append((b, cost))

bus_infos.sort(key=lambda bus_info:bus_info[2])

def dijkstra():
  pq = [(0, start)]
  dist = [INF] * (n + 1)
  dist[start] = 0

  while pq:
    cost, node = heapq.heappop(pq)

    if dist[node] < cost:
      continue

    for next_node, next_cost in graph[node]:
      if dist[next_node] > cost + next_cost:
        dist[next_node] = cost + next_cost
        heapq.heappush(pq, (cost + next_cost, next_node))
  
  return dist[end]


print(dijkstra())
  