# maxheap 과 minheap을 두고
# 중간을 기준으로 작은 부분을 maxheap, 큰 부분을 minheap 으로 넣으면
# maxheap 의 top 과 minheap 의 top 은 중간을 가리키게 됩니다.
# 예를들어 1 3 5 6 9 10 이 들어왔다고 했을 떄
# maxheap: [5 ...]
# minheap: [6 ...]
# 으로 중간값은 5 또는 6인데 작은 값을 구하라고 했으므로 maxheap 의 top 을 출력해주면 됨니다

import sys, heapq
n = int(sys.stdin.readline())
max_heap = []
min_heap = []
result = []

for _ in range(n):
  num = int(sys.stdin.readline())

  if len(max_heap) == len(min_heap):
    if len(max_heap) == 0:
      heapq.heappush(max_heap, -num)
      result.append(-max_heap[0])
      continue
    if min_heap[0] >= num:
      heapq.heappush(max_heap, -num)
      result.append(-max_heap[0])
      continue
    min_num = heapq.heappop(min_heap)
    heapq.heappush(max_heap, -min_num)
    heapq.heappush(min_heap, num)
    result.append(-max_heap[0])
    continue
  if num <= -max_heap[0]:
    mid_num = -heapq.heappop(max_heap)
    heapq.heappush(max_heap, -num)
    heapq.heappush(min_heap, mid_num)
    result.append(-max_heap[0])
    continue
  heapq.heappush(min_heap, num)
  result.append(-max_heap[0])

print('\n'.join(list(map(str, result))))