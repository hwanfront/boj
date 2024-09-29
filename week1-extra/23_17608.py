import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]
prev = -1
cnt = 0
for i in range(len(data) - 1, -1, -1):
  if data[i] > prev:
    cnt += 1
    prev = data[i]

print(cnt)