from abc import ABC, abstractmethod

class AbstractStack(ABC):
  @abstractmethod
  def push(self, data):
    pass
  
  @abstractmethod
  def pop(self):
    pass
    
  @abstractmethod
  def peek(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass