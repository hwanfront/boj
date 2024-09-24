import sys
import heapq
n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().strip() for _ in range(n)]
graph = [[] for _ in range(n)]
degree = [0] * n
pq = []
result = list(range(1, n + 1))


for y in range(n):
  for x in range(n):
    if data[y][x] == '0':
      continue
    graph[x].append(y)
    degree[y] += 1

for i in range(n):
  if degree[i] == 0:
    heapq.heappush(pq, (-i, i))

cnt = n
while pq:
  _, node = heapq.heappop(pq)
  print(node)
  result[node] = cnt
  cnt -= 1
  for next in graph[node]:
    degree[next] -= 1
    if degree[next] == 0:
      heapq.heappush(pq, (-next, next))

for i in range(n):
  if degree[i] != 0:
    print(-1)
    exit()

print(' '.join(map(str, result)))