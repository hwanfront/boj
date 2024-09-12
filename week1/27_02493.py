import sys
n = int(sys.stdin.readline().strip())
tws = list(map(int, sys.stdin.readline().strip().split(' ')))
stack = []
result = [0 for _ in range(n)]

for i in reversed(range(n)):
  tw = tws[i]
  if len(stack) == 0:
    stack.append([tw, i])
    continue
  while len(stack) != 0:
    if stack[-1][0] <= tw:
      [h, idx] = stack.pop()
      result[idx] = i + 1
    else:
      break
  stack.append([tw, i])

print(' '.join(list(map(str, result))))

# []
# [[6, 0]]
# []
# [[9, 1]]
# [[9, 1], [5, 2]]
# [[9, 1]]
# []
# [[7, 3], [4, 4]]
