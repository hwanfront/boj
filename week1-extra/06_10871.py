import sys
n, x = list(map(int, sys.stdin.readline().strip().split(' ')))
data = list(map(int, sys.stdin.readline().strip().split(' ')))
result = []
for num in data:
  if num < x:
    result.append(num)

print(' '.join(map(str, result)))