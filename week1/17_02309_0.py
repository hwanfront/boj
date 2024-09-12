import sys

def find(where: int, cnt: int, sum: int) -> int:
  if sum > 100:
    return 0
  if cnt == 7:
    if sum == 100:
      return 1
    return 0
  for i in range(where, 9):
    if v[i] == 1: continue
    v[i] = 1
    if find(where + 1, cnt + 1, sum + nn[i]) == 1:
      return 1
    v[i] = 0

nn = list(map(int, [sys.stdin.readline().strip() for _ in range(9)]))
v = [0 for _ in range(9)]
result = []

nn.sort()

find(0, 0, 0)

for i in range(0, 9):
  if v[i]:
    result.append(str(nn[i]))
    
print('\n'.join(result))