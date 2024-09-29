import sys
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split(' ')))
result = [data[0]]

def binary_search():
  l = 0
  r = len(result) - 1
  while l <= r:
    mid = (l + r) // 2
    if result[mid] == data[i]:
      return mid
    if result[mid] < data[i]:
      l = mid + 1
    else:
      r = mid - 1
  return l

for i in range(1, n):
  if data[i] > result[-1]:
    result.append(data[i])
    continue
  result[binary_search()] = data[i]

print(len(result))