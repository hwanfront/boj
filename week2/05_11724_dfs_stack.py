import sys
n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
edges = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for a, b in edges:
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  stack = []
  stack.append(start)
  visited[start] = True

  while len(stack) != 0:
    node = stack.pop()
    for next in graph[node]:
      if visited[next]:
        continue
      visited[next] = True
      stack.append(next)

for i in range(1, n + 1):
  if visited[i]:
    continue
  result += 1
  dfs(i)

print(result)
