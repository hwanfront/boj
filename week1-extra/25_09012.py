import sys
n = int(sys.stdin.readline().strip())
result = []

for _ in range(n):
  s = sys.stdin.readline().strip()
  stack = []
  _is = True
  for c in s:
    if c == ')':
      if len(stack) == 0:
        _is = False
        break
      stack.pop()
      continue
    stack.append(c)
  
  result.append('YES' if _is and len(stack) == 0 else 'NO')
  
print('\n'.join(result))