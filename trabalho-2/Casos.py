import csv, os
from AbstractBase import AbstractBase

class Casos(AbstractBase):
    def __init__(self, filename):
        super().__init__(filename)
        self.__casos: dict = {}
    
    def __repr__(self):
        return "Casos: {}".format(self.__casos) 
    
    def getCasos(self) -> dict:
        return self.__casos

    def readFile(self):
        PATH: str = os.getcwd() + "/data/{}".format(self.filename)
        with open(PATH, newline='') as csvfile:
            content: str = csv.reader(csvfile, delimiter=",")
            for index, row in enumerate(content):
                if index == 0:
                    continue
                elif len(self.__casos) <= 0 :
                    self.__casos[index - 1] = tuple(row)
                else:
                    aux = { index-1: tuple(row) }
                    self.__casos.update(aux)