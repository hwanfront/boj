import sys
n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().strip() for _ in range(n)]
result = []

arr = [0] * 81
n = 1
for i in range(1, 81):
  arr[i] = arr[i - 1] + n
  n += 1
  
for s in data:
  sum = 0
  cnt = 0
  for c in s:
    if c == 'X':
      sum += arr[cnt]
      cnt = 0
      continue
    cnt += 1
  sum += arr[cnt]
  result.append(sum)

print('\n'.join(map(str, result)))