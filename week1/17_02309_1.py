import sys

def find():
  for i in range(9):
    if nn[i] >= sum - 100: 
      break
    for j in range(i + 1, 9):
      if nn[i] + nn[j] == sum - 100:
        v[i] = 1
        v[j] = 1
        return

nn = list(map(int, [sys.stdin.readline().strip() for _ in range(9)]))
v = [0 for _ in range(9)]
sum = sum(nn)
result = []

nn.sort()

find()

for i in range(9):
  if v[i] == 1:
    continue
  result.append(nn[i])

print('\n'.join(list(map(str, result))))
  