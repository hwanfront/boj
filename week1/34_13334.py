import sys, heapq
n = int(sys.stdin.readline())
hos = []
for i in range(n):
  hos.append(sorted(list(map(int, sys.stdin.readline().strip().split(' ')))))
d = int(sys.stdin.readline())

hos.sort(key=lambda ho: ho[1])

print(hos)

heap = []
result = 0

for [h, o] in hos:
  heapq.heappush(heap, h)
  while 1:
    if len(heap) == 0:
      break
    if heap[0] >= o - d:
      break
    heapq.heappop(heap)
  result = max(result, len(heap))

print(str(result))
