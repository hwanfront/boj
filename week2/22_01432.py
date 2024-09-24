# 1. 입력은 인접 행렬 형태로, V1 -> V2 로 연결된 간선이 있다는 의미
# 2. 만약 V1 -> V2 로 연결된 간선이 있다면, V2가 V1보다 큼. 간선은 항상 큰 값을 가리킨다는 뜻
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

# 위상정렬을 통해 간선을 제거했지만 아직 남은 간선이 있다면 사이클이 존재한다는 뜻
for i in range(n):
  if degree[i] != 0:
    print(-1)
    exit()

print(' '.join(map(str, result)))