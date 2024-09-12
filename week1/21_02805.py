import sys
[n, m] = list(map(int, sys.stdin.readline().strip().split(' ')))
trees = list(map(int, sys.stdin.readline().strip().split(' ')))

def check(height, trees, m):
  sum = 0
  for tree in trees:
    if tree <= height:
      continue
    sum += tree - height
  if sum >= m:
    return True
  return False

def bs(trees, m):
  l = 0
  r = max(trees)
  result = 0
  while l <= r:
    mid = (l + r) // 2
    if check(mid, trees, m):
      result = max(result, mid)
      l = mid + 1
    else:
      r = mid - 1
  return result

print(bs(trees, m))

