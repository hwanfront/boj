from abc import ABC, abstractmethod

class PriorityQueue(ABC):
  @abstractmethod
  def is_empty(self):
    pass

  @abstractmethod
  def top(self):
    pass

  @abstractmethod
  def push(self, data):
    pass

  @abstractmethod
  def pop(self):
    pass
