from abstract_queue import AbstractQueue
  
class Queue(AbstractQueue):
  def __init__(self):
    self.list = []
    self.rm_idx = -1
  
  def enqueue(self, data):
    self.list.append(data)
  
  def dequeue(self):
    if len(self.list) == self.rm_idx + 1:
      return None
    self.rm_idx += 1
    return self.list[self.rm_idx]
  
  def is_empty(self):
    return len(self.list) == self.rm_idx + 1
  
if __name__ == "__main__":
  q = Queue()

  for i in range(3):
    data = chr(ord("A") + i)
    q.enqueue(data)
    print(f"Enqueue data = {data}")
  print()

  while not q.is_empty():
    print(f"Dequeue data = {q.dequeue()}")