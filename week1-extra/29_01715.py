import sys
import heapq
n = int(sys.stdin.readline().strip())
pq = [int(sys.stdin.readline().strip()) for _ in range(n)]
heapq.heapify(pq)
result = 0

while len(pq) != 1:
  num1 = heapq.heappop(pq)
  num2 = heapq.heappop(pq)
  result += num1 + num2
  heapq.heappush(pq, num1 + num2)

print(result)
