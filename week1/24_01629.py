import sys
[a, b, c] = list(map(int, sys.stdin.readline().strip().split(' ')))
obj = {}
obj[1] = a % c

def go(a, b):
  if obj.get(b) == None:
    obj[b] = (go(a, b // 2) * go(a, b - (b // 2))) % c
  return obj[b]

print(go(a, b))