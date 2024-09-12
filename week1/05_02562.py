import sys
data = list(map(int, [sys.stdin.readline().strip() for _ in range(9)]))
max_value = -1
max_idx = -1

for i in range(0, 9):
  if max_value > data[i]: continue
  max_value = data[i]
  max_idx = i + 1

print(f'{max_value}\n{max_idx}')
