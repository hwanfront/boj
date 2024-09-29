import sys
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split(' ')))
data.sort()
ss=30**9
l = 0
r = n - 1
lv = -1
rv = -1

if data[0] >= 0:
  print(f'{data[0]} {data[1]}')
  exit()

if data[n - 1] <= 0:
  print(f'{data[n - 2]} {data[n - 1]}')
  exit()

while l != r:
  if ss > abs(data[l] + data[r]):
    ss = min(ss, abs(data[l] + data[r]))
    lv = data[l]
    rv = data[r]
  if data[l] + data[r] < 0:
    l += 1
  else:
    r -= 1

print(f'{lv} {rv}')