import sys
n, c = tuple(map(int, sys.stdin.readline().strip().split(' ')))
data = [int(sys.stdin.readline().strip()) for _ in range(n)]
result = 10**9
l = 0
r = 10**9
data.sort()

def check(target, data):
  global result
  cnt = 1
  prev = data[0]
  _is = False
  for i in range(1, n):
    if data[i] - prev == target:
      _is = True
    if data[i] - prev >= target:
      cnt += 1
      prev = data[i]
  if cnt >= c:
    if _is:
      result = target
    return True
  return False

while l <= r:
  mid = (l + r) // 2
  if check(mid, data):
    l = mid + 1
  else:
    r = mid - 1

print(result)