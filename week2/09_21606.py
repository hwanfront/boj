import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().strip())
a = '0' + sys.stdin.readline().strip()
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1)
result = 0

for _ in range(n - 1):
  [f, t] = list(map(int, sys.stdin.readline().strip().split(' ')))
  graph[f].append(t)
  graph[t].append(f)

def dfs(now):
  global result, cnt
  for next in graph[now]:
    if visited[next]:
      continue
    if a[next] == '1':
      cnt += 1
      continue
    visited[next] = True
    dfs(next)


for i in range(1, n + 1):
  if visited[i]:
    continue
  if a[i] == '0':
    cnt = 0
    visited[i] = True
    dfs(i)
    result += cnt * (cnt - 1)
  else:
    for next in graph[i]:
      if a[next] == '0':
        continue
      result += 1

print(result)