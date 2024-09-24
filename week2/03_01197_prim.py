import sys
import heapq
v, e = list(map(int, sys.stdin.readline().strip().split(' ')))
edges = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(e)]
graph = [[] for _ in range(v + 1)]

for a, b, c in edges:
  graph[a].append((b, c))
  graph[b].append((a, c))

def prim(start):
  min_heap = [(0, start)]
  visited = [False] * (v + 1)
  result = 0

  while len(min_heap) != 0:
    cost, node = heapq.heappop(min_heap)

    if visited[node]:
      continue

    visited[node] = True
    result += cost

    for next, next_cost in graph[node]:
      if visited[next]:
        continue
      heapq.heappush(min_heap, (next_cost, next))   

  return result 

print(prim(1))