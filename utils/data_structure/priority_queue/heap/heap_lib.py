import os
import sys
import heapq
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from priority_queue import PriorityQueue

class Heap(PriorityQueue):
  def __init__(self, compare):
    self.heap = []

  def is_empty(self):
    return len(self.heap) == 0
  
  def top(self):
    if len(self.heap) == 0:
      return None
    return self.heap[-1]
  
  def push(self, data):
    heapq.heappush(self.heap, data)

  def pop(self):
    if self.is_empty():
      return None
    return heapq.heappop(self.heap)

