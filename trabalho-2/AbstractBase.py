from abc import ABC, ABCMeta, abstractmethod 
  
class AbstractBase(object, metaclass=ABCMeta): 
    @abstractmethod
    def __init__(self, filename):
        self.filename = filename
    
    @abstractmethod
    def readFile(self):
        pass  