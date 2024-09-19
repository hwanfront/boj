import sys
n = int(sys.stdin.readline().strip())
result = []
for _ in range(n):
  a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
  result.append(a + b)
print('\n'.join(map(str, result)))