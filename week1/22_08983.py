# 사대 -> 동물 으로 찾으려면 n**2 인데 
# 동물 -> 사대 로 찾아서 가능한 사대를 이분탐색으로 찾으면 nlogn이라 연산 횟수가 많이 줄겠죠?

import sys
[m, n, l] = list(map(int, sys.stdin.readline().strip().split(' ')))
s_xx = list(map(int, sys.stdin.readline().strip().split(' ')))
pos = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
s_xx.sort()

result = 0

def check(x, y, s_x, l):
  return abs(s_x - x) + y <= l

def bs(x, y, s_xx, m, l):
  l = 0
  r = m - 1
  while l <= r:
    mid = (l + r) // 2
    if check(x, y, s_xx[mid], l):
      return True
    if x > s_xx[mid]:
      l = mid + 1
    else:
      r = mid - 1
  return False

for [x, y] in pos:
  if bs(x, y, s_xx, m, l):
    result += 1

print(result)
