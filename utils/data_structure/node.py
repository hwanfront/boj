class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

head = Node(1)
head.next = Node(3)
head.next.next = Node(3)

node = head
while node:
  node = node.next
node.next = Node(4)