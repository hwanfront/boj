# pypy3 에서는 풀리는데 python3에선 시간초과 나오네요
import sys

def go(y):
  global result
  if y == n:
    result += 1
    return
  for x in range(0, n):
    _is = 1
    for i in range(0, y):
      if x == v[i] or abs(x - v[i]) == abs(y - i): 
        _is = 0
        break
    if not _is: continue
    v.append(x)
    go(y + 1)
    v.pop()
    
n = int(sys.stdin.readline().strip())
v = []
result = 0
go(0)
print(result)
