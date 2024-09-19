from abstract_stack import AbstractStack

class Stack(AbstractStack):
  def __init__(self):
    self.list = []

  def push(self, data):
    self.list.append(data)

  def pop(self):
    if len(self.list) == 0:
      return None
    return self.list.pop()
  
  def peek(self):
    if len(self.list) == 0:
      return None
    return self.list[-1]
  
  def is_empty(self):
    return len(self.list) == 0

  
if __name__ == "__main__":
  ls = Stack()

  for i in range(3):
      ls.push(chr(ord("A") + i))
      print(f"list stack Push data = {ls.peek()}")
  print()

  print(f"list stack Peek data = {ls.peek()}")

  print()
  while not ls.is_empty():
      print(f"list stack Pop data = {ls.pop()}")
  print()

  print(f"list stack Peek data = {ls.peek()}")