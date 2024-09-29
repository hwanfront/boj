import sys
[a, b, c] = list(map(int, sys.stdin.readline().strip().split(' ')))
obj = {}
obj[1] = a % c

def go(a, b):
  if b == 1:
    return a % c
  value = go(a, b // 2)
  if b % 2 == 0:
    return (value * value) % c
  else:
    return (value * value * a) % c
  
print(go(a, b))