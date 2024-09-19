import sys
n = int(sys.stdin.readline().strip())
result = []
for i in range(n):
  result.append('*' * (i + 1))
print('\n'.join(result))