import sys
n = int(sys.stdin.readline().strip())
arr = [0] * 10001
for i in range(n):
  arr[int(sys.stdin.readline().strip())] += 1

for i in range(1, 10001):
  if arr[i] > 0:
    for j in range(arr[i]):
      print(i)
