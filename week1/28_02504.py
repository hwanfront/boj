# ( () [[]] ) 는 결국 (()) + ([[]]) 와 같음
# 2 * (2 + (3 * 3)) 
# = (2 * 2) + (2 * (3 * 3))
import sys
input = sys.stdin.readline().strip()
stack = []
result = 0
sum = 1
is_closed = False
incorrect = False

for c in input:
  print(stack)
  if len(stack) == 0 and (c == ']' or c == ')'):
    incorrect = True
    break
  
  if c == '[':
    is_closed = False
    stack.append(c)
    sum *= 3
    continue
  
  if c == '(':
    is_closed = False
    stack.append(c)
    sum *= 2
    continue

  if c == ']':
    if stack[-1] == '[':
      if not is_closed:
        result += sum
        is_closed = True
      stack.pop()
      sum //= 3
      continue
    incorrect = True
    break

  if c == ')':
    if stack[-1] == '(':
      if not is_closed:
        result += sum
        is_closed = True
      stack.pop()
      sum //= 2
      continue
    incorrect = True
    break

if incorrect or len(stack) > 0:
  print(0)
else:
  print(str(result))