import sys, heapq
n = int(sys.stdin.readline().strip())
heap = []
result = []
for i in range(n):
  info = int(sys.stdin.readline().strip())
  if info == 0:
    if len(heap) == 0:
      result.append('0')
      continue
    result.append(str(-heapq.heappop(heap)))
    continue
  heapq.heappush(heap, -info)

print('\n'.join(result))
