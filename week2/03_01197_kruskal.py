import sys
sys.setrecursionlimit(10**6)

v, e = list(map(int, sys.stdin.readline().strip().split(' ')))
edges = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(e)]
parent = list(range(v + 1))
result = 0

edges.sort(key=lambda a:a[2])

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)

  if x == y: return
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for a, b, c in edges:
  if find(a) == find(b):
    continue
  union(a, b)
  result += c

print(result)