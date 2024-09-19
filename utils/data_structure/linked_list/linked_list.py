class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def __len__(self):
    return self.length

  def __contains__(self, target):
    if self.head is None:
      return False
    node = self.head
    while node is not None:
      if node.data == target:
        return True
      node = node.next
    return False

  # linked list 처음 데이터 추가
  # 1. head 가 비어있으면 생성한 노드를 head 에 할당
  # 2. head 가 이미 있으면 
  # 2-1. [new node]의 next에 [head node]를 할당
  # 2-2. head에 [new node]를 할당
  def appendleft(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      node = Node(data)
      node.next = self.head
      self.head = node
    self.length += 1

  # linked list 끝 데이터 추가
  # 1. head 가 비어있으면 생성한 노드를 head 에 할당
  # 2. head 가 이미 있으면 
  # 2-1. 임시 노드를 만들어 마지막 노드까지 이동
  # 2-2. 마지막 노드의 next에 [new node] 할당
  def append(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      node = self.head
      while node.next is not None:
        node = node.next
      node.next = Node(data)
    self.length += 1

  # linked list 처음 데이터 삭제
  # 1. head 가 비어있으면 None 반환
  # 2. head 가 이미 있으면
  # 2-1. 임시 노드를 만들어 head node 를 할당
  # 2-2. head 에 head 의 다음 노드를 할당
  # 2-3. 임시 노드의 값을 반환
  def popleft(self):
    if self.head is None:
      return None
    node = self.head
    self.head = self.head.next
    self.length -= 1
    return node.data

  # linked list 끝 데이터 삭제
  # 1. head 가 비어있으면 None 반환
  # 2. head 가 이미 있으면
  # 2-1. 임시 노드와 이전 노드 생성
  # 2-2. 임시 노드의 next 노드가 None 일때까지 이동
  # 2-3-1. 이전 노드가 None 이면 head 에 None 할당
  # 2-3-2. 이전 노드가 None 이 아니면 이전 노드의 next 에 None 할당
  def pop(self):
    if self.head is None:
      return None
    prev = None
    node = self.head
    while node.next is not None:
      prev = node
      node = node.next
    if prev is None:
      self.head = None
    else:
      prev.next = None
    self.length -= 1
    return node.data

  # linked list 특정 데이터 삭제
  # 1. head 가 비어있으면 False 반환
  # 2. head 가 이미 있으면
  # 2-1. 임시 노드와 이전 노드 생성
  # 2-2. 임시 노드의 값이 타겟과 같을때까지 이동
  # 2-3-1. node 가 None 이면 False 반환
  # 2-3-2-1. node 가 head 와 같다면 head 에 head 의 다음 노드 할당
  # 2-3-2-2. node 가 head 와 같지 않다면 이전 노드의 next 에 임시 노드의 다음 노드 할당
  def remove(self, target):
    if self.head is None:
      return False
    node = self.head
    while node is not None and node.data != target:
      prev = node
      node = node.next
    if node is None:
      return False
    if node == self.head:
      self.head = self.head.next
    else:
      prev.next = node.next
    self.length -= 1
    return True

  # linked list 특정 위치에 데이터 추가
  # 1. idx 가 0 보다 작거나 같으면 appendleft
  # 2. idx 가 현재 길이보다 크거나 같으면 append
  # 3. 임시 노드 생성
  # 3-1. idx - 1 만큼 임시 노드를 next 로 이동
  # 3-2. [new node] 를 생성하고 [new node] 의 next 에 임시 노드의 다음 노드를 할당 
  # 3-3. 임시 노드의 next 에 [new node] 할당
  def insert(self, idx, data):
    if idx <= 0:
      self.appendleft(data)
    elif idx >= self.length:
      self.append(data)
    else:
      node = self.head
      for _ in range(idx - 1):
        node = node.next
      new_node = Node(data)
      new_node.next = node.next
      node.next = new_node
      self.length += 1

if __name__ == "__main__":
  import random
  data = list(range(10, 15))
  random.shuffle(data)
  my_list = LinkedList()
  for i in data:
    my_list.append(i)
  print(f"연결 리스트의 상태\n{my_list}")
  print()
  for _ in range(len(my_list)):
    print(f"{my_list.pop()}를(을) 꺼낸 후: 길이 = {len(my_list)}, {my_list}")
  print(f"연결 리스트가 비었을 때 꺼낸 값은 {my_list.pop()}")