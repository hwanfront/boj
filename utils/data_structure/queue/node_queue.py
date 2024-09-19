from abstract_queue import AbstractQueue

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue(AbstractQueue):
  def __init__(self):
    self.front = None
    self.rear = None
  
  # 1. front 가 None 인 경우 front 와 rear 에 new node 를 할당
  # 2. front 가 None 이 아닌 경우
  # 2-1. 임시 노드에 new node 할당
  # 2-2. rear node 의 next 에 임시 노드(new node) 할당
  # 2-3. rear 에 임시 노드(new node) 할당
  def enqueue(self, data):
    if self.front is None:
      self.front = self.rear = Node(data)
    else:
      node = Node(data)
      self.rear.next = node
      self.rear = node
  
  # 1. front 가 None 인 경우 None 반환
  # 2. front 가 None 이 아닌 경우
  # 2-1. front 와 rear 가 같다면 front 와 rear 에 None 을 할당
  # 2-2. front 와 rear 가 같지 않다면 front 에 front next node 를 할당
  def dequeue(self):
    if self.front is None:
      return None
    node = self.front
    if self.front == self.rear:
      self.front = self.rear = None
    else:
      self.front = self.front.next
    return node.data
  
  def is_empty(self):
    return self.front is None
  
    
if __name__ == "__main__":
  q = Queue()

  for i in range(3):
    data = chr(ord("A") + i)
    q.enqueue(data)
    print(f"Enqueue data = {data}")
  print()

  while not q.is_empty():
    print(f"Dequeue data = {q.dequeue()}")