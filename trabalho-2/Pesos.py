import csv, os
from AbstractBase import AbstractBase

class Pesos(AbstractBase):
    def __init__(self, filename):
        super().__init__(filename)
        self.__pesos: dict = {}
    
    def __repr__(self):
        return "Pesos: {}".format(self.__pesos) 
    
    def readFile(self):
        aux: dict = {}
        PATH: str = os.getcwd() + "/data/{}".format(self.filename)
        with open(PATH, newline='') as csvfile:
            content: str = csv.reader(csvfile, delimiter=",")
            for index, row in enumerate(content):
                if index == 0:
                    continue
                elif len(self.__pesos) <= 0:
                    self.__pesos[row[0]] = row[1]
                else:
                    aux = {row[0]:row[1]}
                    self.__pesos.update(aux)