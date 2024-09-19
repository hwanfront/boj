import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from priority_queue import PriorityQueue

class Heap(PriorityQueue):
  def __init__(self, compare):
    self.heap = []
    self.compare = compare

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
      if self.compare(pd, cd):
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
      bi = lci if rcd is None or self.compare(lcd, rcd) else rci
      bd = self.heap[bi]
      if self.compare(pd, bd):
        break
      self.heap[pi] = bd
      pi = bi
    self.heap[pi] = pd

def cb(a, b):
  return a[0] > b[0]
  
def max_cb(a, b):
  return a > b

def min_cb(a, b):
  return a < b

heap = Heap(cb)
max_heap = Heap(max_cb)
min_heap = Heap(min_cb)

heap.push([15, 'a'])
heap.push([3, 'b'])
heap.push([6, 'c'])
heap.push([5, 'd'])
heap.push([8, 'e'])
heap.push([10, 'f'])
heap.push([22, 'g'])
heap.push([14, 'h'])

max_heap.push(15)
max_heap.push(3)
max_heap.push(6)
max_heap.push(5)
max_heap.push(8)
max_heap.push(10)
max_heap.push(22)
max_heap.push(14)

min_heap.push(15)
min_heap.push(3)
min_heap.push(6)
min_heap.push(5)
min_heap.push(8)
min_heap.push(10)
min_heap.push(22)
min_heap.push(14)

print('---------------- heap -----------------')
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop()[1])
print(heap)
print(heap.pop())
print()

print('-------------- maxheap ----------------')
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print(max_heap)
print(max_heap.pop())
print()

print('-------------- minheap ----------------')
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
print(min_heap)
print(min_heap.pop())
