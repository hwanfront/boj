import sys
n, k = tuple(map(int, sys.stdin.readline().strip().split(' ')))
data = tuple(map(int, list(sys.stdin.readline().strip())))
stack = []
for i in range(n):
  if not stack:
    stack.append(data[i])
    continue
  while True:
    if k == 0:
      break
    if not stack:
      break
    if stack[-1] >= data[i]:
      break

    stack.pop()
    k -= 1

  stack.append(data[i])
  if k == 0:
    break

stack.extend(data[i + 1:])
if k == 0:
  print(''.join(map(str, stack)))
else:
  print(''.join(map(str, stack[:-k])))
