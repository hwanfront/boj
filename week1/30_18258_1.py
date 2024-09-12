from collections import deque
import sys

n = int(sys.stdin.readline().strip())
cmds = [sys.stdin.readline().strip().split(' ') for _ in range(0, n)]
deq = deque()
result = []

for cmd in cmds:
  if cmd[0] == 'push':
    deq.append(cmd[1])
    continue
  if cmd[0][0] == 'p':
    if len(deq) == 0:
      result.append(-1)
      continue
    result.append(deq.popleft())
    continue
  if cmd[0][0] == 's':
    result.append(len(deq))
    continue
  if cmd[0][0] == 'e':
    if len(deq) == 0:
      result.append(1)
      continue
    result.append(0)
    continue
  if cmd[0][0] == 'f':
    if len(deq) == 0:
      result.append(-1)
      continue
    result.append(deq[0])
    continue
  if len(deq) == 0:
    result.append(-1)
    continue
  result.append(deq[len(deq) - 1])
  
print('\n'.join(list(map(str, result))))
