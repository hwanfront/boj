import sys
n = int(sys.stdin.readline())
data = []
stack = []
for _ in range(n):
  x, r = tuple(map(int, sys.stdin.readline().strip().split(' '))) 
  data.append((x - r, -(x + r), x - r, x + r))
data.sort()

result = 1

for _, _, s, e in data:
  if not stack:
    stack.append([s, e, -1, 0])
    continue
  if s < stack[-1][1]:
    stack.append([s, e, len(stack) - 1, 0])
    continue
  while len(stack) > 1 and stack[-1][1] <= s:
    item = stack.pop()
    if item[3] == item[1] - item[0]:
      result += 1
    result += 1
    if stack[-1][0] <= item[0] and item[1] <= stack[-1][1]:
      stack[item[2]][3] += item[1] - item[0]
  stack.append([s, e, len(stack) - 1, 0])

while len(stack) > 1:
  item = stack.pop()
  if item[3] == item[1] - item[0]:
    result += 1
  result += 1
  if stack[-1][0] <= item[0] and item[1] <= stack[-1][1]:
    stack[item[2]][3] += item[1] - item[0]

item = stack.pop()
if item[3] == item[1] - item[0]:
  result += 1
result += 1
print(result)