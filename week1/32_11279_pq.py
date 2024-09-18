import sys

class MaxHeap:
  def __init__(self):
    self.heap = []


  def push(self, data):
    self.heap.append(data)
    self.heapify_up()
    return
  
  def heapify_up(self):
    ci = len(self.heap) - 1
    cd = self.heap[ci]
    while ci > 0:
      pi = (ci - 1) // 2
      pd = self.heap[pi]
      if pd > cd:
        break
      self.heap[ci] = pd
      ci = pi
    self.heap[ci] = cd
  
  def pop(self):
    if len(self.heap) == 0:
      return 0
    data = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    if len(self.heap) > 0:
      self.heapify_down()
    return data
  
  def heapify_down(self):
    pi = 0
    pd = self.heap[pi]
    while pi < len(self.heap):
      li = pi * 2 + 1
      ri = pi * 2 + 2
      if li >= len(self.heap):
        break
      ld = self.heap[li]
      rd = self.heap[ri] if ri < len(self.heap) else None
      bi = li if rd is None or ld > rd else ri
      bd = self.heap[bi]
      if bd < pd:
        break
      self.heap[pi] = bd
      pi = bi
    self.heap[pi] = pd

n = int(sys.stdin.readline().strip())
heap = MaxHeap()
result = []

for _ in range(n):
  cmd = sys.stdin.readline().strip()
  if cmd == '0':
    result.append(heap.pop())
    continue
  heap.push(int(cmd))

print('\n'.join(map(str, result)))
