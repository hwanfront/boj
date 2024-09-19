import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from priority_queue import PriorityQueue

class MaxHeap(PriorityQueue):
  def __init__(self):
    self.heap = []

  def is_empty(self):
    return len(self.heap) == 0
  
  def top(self):
    if len(self.heap) == 0:
      return None
    return self.heap[-1]
  
  def push(self, data):
    self.heap.append(data)
    self.heapify_up()
  
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
      return None
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
      lci = pi * 2 + 1
      rci = pi * 2 + 2
      if lci >= len(self.heap):
        break
      lcd = self.heap[lci]
      rcd = self.heap[rci] if rci < len(self.heap) else None
      bi = lci if rcd is None or lcd > rcd else rci
      bd = self.heap[bi]
      if pd > bd:
        break
      self.heap[pi] = bd
      pi = bi
    self.heap[pi] = pd
  
heap = MaxHeap()
heap.push(15)
heap.push(3)
heap.push(6)
heap.push(5)
heap.push(8)
heap.push(10)
heap.push(22)
heap.push(14)

print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
print(heap)
print(heap.pop())
