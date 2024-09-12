# pypy3 에서는 풀리는데 python3에선 시간초과 나오네요

import sys
n = int(sys.stdin.readline().strip())
cmds = [sys.stdin.readline().strip().split(' ') for _ in range(0, n)]
rm_idx = -1
q = []
result = []

for cmd in cmds:
  if cmd[0] == 'push':
    q.append(cmd[1])
    continue
  if cmd[0][0] == 'p':
    if len(q) == rm_idx + 1:
      result.append('-1')
      continue
    result.append(q[rm_idx + 1])
    rm_idx += 1
    continue
  if cmd[0][0] == 's':
    result.append(str(len(q) - (rm_idx + 1)))
    continue
  if cmd[0][0] == 'e':
    if len(q) == rm_idx + 1:
      result.append('1')
      continue
    result.append('0')
    continue
  if cmd[0][0] == 'f':
    if len(q) == rm_idx + 1:
      result.append('-1')
      continue
    result.append(q[rm_idx + 1])
    continue
  if len(q) == rm_idx + 1:
    result.append('-1')
    continue
  result.append(q[-1])
  
print('\n'.join(result))