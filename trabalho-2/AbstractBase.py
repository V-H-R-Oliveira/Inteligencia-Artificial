from abc import ABC, ABCMeta, abstractmethod 
from Persistence import Persistence

class AbstractBase(object, metaclass=ABCMeta): 
    @abstractmethod
    def __init__(self, filename: str):
        self.filename: str = filename
        self.dbHandler: Persistence = Persistence()
    
    @abstractmethod
    def readFile(self):
        raise NotImplementedError
    
    @abstractmethod
    def persist(self):
        raise NotImplementedError