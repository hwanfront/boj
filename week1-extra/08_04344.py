import sys
from statistics import mean
c = int(sys.stdin.readline().strip())
ss = []
result = []

for _ in range(c):
  data = list(map(int, sys.stdin.readline().strip().split(' ')))
  ss.append(data[1:])

for arr in ss:
  avg = mean(arr)
  cnt = 0
  for s in arr:
    if s > avg:
      cnt += 1
  result.append(f'{((cnt / len(arr)) * 100):.3f}%')

print('\n'.join(result))