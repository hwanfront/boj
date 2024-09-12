import sys
t = int(sys.stdin.readline().strip())
tc = [sys.stdin.readline().strip() for _ in range(t)]
result = ''

for i in range(t):
  [r, str] = tc[i].split(' ')
  p = ''
  for c in str:
    p += (c * int(r))
  result += p + '\n'

print(result.rstrip())
