import sys
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None
  
  def add(self, value, left = None, right = None):
    if self.root is None:
      self.root = Node(value)
      if left is not None:
        self.root.left = Node(left)
      if right is not None:
        self.root.right = Node(right)
    else:
      self.search(self.root, value, left, right)

  def search(self, root, value, left, right):
    if root is None:
      return
    elif root.value == value:
      if left is not None:
        root.left = Node(left)
      if right is not None:
        root.right = Node(right)
    else:
      self.search(root.left, value, left, right)
      self.search(root.right, value, left, right)


  def order(self, root):
    preo.append(root.value)
    if root.left is not None:
      self.order(root.left)
    ino.append(root.value)
    if root.right is not None:
      self.order(root.right)
    posto.append(root.value)

n = int(sys.stdin.readline().strip())
tree = Tree()
preo = []
ino = []
posto = []

for _ in range(n):
  v, l, r = sys.stdin.readline().strip().split(' ')
  if l == '.':
    l = None
  if r == '.':
    r = None
  tree.add(v, l, r)

tree.order(tree.root)

print(''.join(preo), ''.join(ino), ''.join(posto),sep='\n')