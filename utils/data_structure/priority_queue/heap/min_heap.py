import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from priority_queue import PriorityQueue

class MinHeap(PriorityQueue):
  def __init__(self):
    self.heap = []

  def is_empty(self):
    return len(self.heap) == 0
  
  def top(self):
    if len(self.heap) == 0:
      return None
    return self.heap[-1]
  
  # min heap 데이터 추가
  # 1. 배열의 마지막에 데이터를 추가합니다
  # 2. heapifyup 실행
  def push(self, data):
    self.heap.append(data)
    self.heapify_up()
  
  # heapifyup
  # 1. ci 에 배열의 마지막 인덱스, cd 에 새 요소 할당
  # 2. ci 가 0 보다 크면
  # 2-1. pi 는 ci 의 부모요소 인덱스, pd 는 heap의 pi번째요소 할당
  # 2-2. 부모요소가 자식요소보다 크면
  # 2-2-1. heap의 ci 위치에 부모 요소 할당
  # 2-2-2. ci 를 부모 인덱스로 교체
  # 2-2-3. 반복
  # 2-3. 부모요소가 자식요소보다 작으면
  # 2-3-1. break 반복문 종료
  # 4. heap의 ci 위치에 새 요소 할당
  def heapify_up(self):
    ci = len(self.heap) - 1
    cd = self.heap[ci]
    while ci > 0:
      pi = (ci - 1) // 2
      pd = self.heap[pi]
      if pd < cd:
        break
      self.heap[ci] = pd
      ci = pi
    self.heap[ci] = cd
    
  # min heap 데이터 삭제
  # 0. 힙이 비어있으면 None 을 반환
  # 1. 임시 변수에 반환될 가장 작은 값(0번째 요소)을 할당
  # 2. 힙의 0번째 인덱스에 가장 마지막 요소를 할당
  # 3. 힙의 크기가 0보다 크면 heapify down 실행
  # 4. 가장 작은 값 반환
  def pop(self):
    if len(self.heap) == 0:
      return None
    data = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    if len(self.heap) > 0:
      self.heapify_down()
    return data
  
  # heapify down
  # 1. pi 에 0, pd 에 0번째 요소(마지막 요소 였던) 할당
  # 2. pi 가 힙의 크기보다 작으면
  # 2-1. 현재부모요소 의 왼쪽과 오른쪽요소 의 인덱스 할당
  # 2-2. 왼쪽요소 가 힙의 범위를 벗어나면 반복문 종료
  # 2-3. 왼쪽요소 를 임시변수에 할당
  # 2-4. 오른쪽요소 의 인덱스가 힙의 범위를 벗어나면 None, 아니면 오른쪽요소 를 임시변수에 할당
  # 2-5. 오른쪽요소 가 None 이거나 오른쪽요소 가 더 크면 최적요소인덱스는 왼쪽요소인덱스, 아니면 오른쪽요소인덱스
  # 2-6. 최적요소가 현재부모요소 보다 크면 반복문 종료
  # 2-7. 최적요소가 현재부모요소 보다 작거나 같으면
  # 2-7-1. 현재부모요소인덱스 위치에 최적요소 할당
  # 2-7-2. 현재부모요소인덱스 에 최적요소인덱스 할당
  # 2-7-3. 반복
  # 3. 현재부모요소인덱스 에 마지막 요소 였던 것 할당
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
      bi = lci if rcd is None or lcd < rcd else rci
      bd = self.heap[bi]
      if pd < bd:
        break
      self.heap[pi] = bd
      pi = bi
    self.heap[pi] = pd
  
heap = MinHeap()
heap.push(15)
heap.push(3)
heap.push(6)
heap.push(5)
heap.push(8)
heap.push(8)
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
