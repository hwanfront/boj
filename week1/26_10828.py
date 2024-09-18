import sys
n = int(sys.stdin.readline().strip())
cc = [sys.stdin.readline().strip().split(' ') for _ in range(n)]
stack = []
result = []
for c in cc:
  if c[0] == 'push':
    stack.append(int(c[1]))
  elif c[0][0] == 'p':
    if len(stack) == 0:
      result.append(-1)
      continue
    result.append(stack.pop())
  elif c[0][0] == 't':
    if len(stack) == 0:
      result.append(-1)
      continue
    result.append(stack[len(stack) - 1])
  elif c[0][0] == 's':
    result.append(len(stack))
  else:
    if len(stack) == 0:
      result.append(1)
      continue
    result.append(0)

print('\n'.join(list(map(str, result))))