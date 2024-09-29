import sys
n = int(sys.stdin.readline().strip())
stack = []

for _ in range(n):
  num = int(sys.stdin.readline().strip())
  if num == 0:
    stack.pop()
    continue
  stack.append(num)

print(sum(stack))