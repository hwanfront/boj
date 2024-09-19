from abc import ABC, abstractmethod

class AbstractQueue(ABC):
  @abstractmethod
  def enqueue(self, data):
    pass

  @abstractmethod
  def dequeue(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass