import sys
n = int(sys.stdin.readline())
data = tuple(map(int, sys.stdin.readline().strip().split(' ')))
visited = [False] * n
result = 0

def dfs(prev, total, cnt):
  global result
  if cnt == n:
    result = max(result, total)
    return
  for i in range(n):
    if visited[i]:
      continue
    visited[i] = True
    dfs(data[i], total + abs(prev - data[i]), cnt + 1)
    visited[i] = False

for i in range(n):
  visited[i] = True
  dfs(data[i], 0, 1)
  visited[i] = False

print(result)