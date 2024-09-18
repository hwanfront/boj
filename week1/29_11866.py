import sys
from queue import Queue
[n, k] = list(map(int, sys.stdin.readline().strip().split(' ')))
q = Queue()
result = []

for i in range(1, n + 1):
  q.put(i)

while not q.empty():
  for i in range(1, k):
    q.put(q.get())
  result.append(q.get())

print(f'<{", ".join(list(map(str, result)))}>')