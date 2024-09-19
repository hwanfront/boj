from abstract_stack import AbstractStack

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack(AbstractStack):
  def __init__(self):
    self.top = None
  
  # 1. top 이 None 이라면 top 에 new node 생성 및 할당
  # 2. top 이 None 이 아니라면
  # 2-1. new node 생성 후 top 에 할당된 node 를 new node 의 next 에 할당
  # 2-2. top 에 new node 할당
  def push(self, data):
    if self.top is None:
      self.top = Node(data)
    else:
      newNode = Node(data)
      newNode.next = self.top
      self.top = newNode
  
  # 1. top 이 None 이라면 None 반환
  # 2. top 이 None 이 아니라면
  # 2-1. top node 의 값을 저장
  # 2-2. top 에 top node 의 next node 를 할당
  def pop(self):
    if self.top is None:
      return False
    data = self.top.data
    self.top = self.top.next
    return data
  
  def peek(self):
    if self.top is None:
      return None
    return self.top.data
  
  def is_empty(self):
    return self.top is None
  
if __name__ == "__main__":
  ns = Stack()

  for i in range(3):
      ns.push(chr(ord("A") + i))
      print(f"node stack Push data = {ns.peek()}")
  print()

  print(f"node stack Peek data = {ns.peek()}")
  print()

  while not ns.is_empty():
      print(f"node stack Pop data = {ns.pop()}")
  print()

  print(f"node stack Peek data = {ns.peek()}")