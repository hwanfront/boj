# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

import sys
from queue import Queue
n, m, v = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result1 = []
result2 = []

for i in range(m):
  [a, b] = list(map(int, sys.stdin.readline().strip().split()))
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n + 1):
  graph[i].sort()

def dfs(start):
  stack = []
  stack.append(start)

  while len(stack) != 0:
    now = stack.pop()
    if visited[now]: 
      continue
    visited[now] = True
    result1.append(now)
    for next in graph[now]:
      if visited[next]:
        continue
      stack.append(next)

def bfs(start):
  queue = Queue()
  queue.put(start)
  visited[start] = True

  while not queue.empty():
    now = queue.get()
    result2.append(now)
    for next in graph[now]:
      if visited[next]:
        continue
      visited[next] = True
      queue.put(next)

bfs(v)

visited = [False] * (n + 1)
# stack 에 추가할때에는 반대로
for i in range(1, n + 1):
  graph[i].reverse()

dfs(v)

print(' '.join(map(str, result1)))
print(' '.join(map(str, result2)))